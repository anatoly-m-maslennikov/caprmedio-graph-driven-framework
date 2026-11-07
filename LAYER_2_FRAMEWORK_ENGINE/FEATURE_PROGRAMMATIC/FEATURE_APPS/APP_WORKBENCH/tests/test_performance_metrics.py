# CA-E-677@18
# CA-E-780@7
"""Prove performance violations fail after reporting, without waiting in tests."""
from contextlib import redirect_stdout
import io
import json
import unittest
from unittest.mock import patch

from workbench_performance_metrics import record_performance


class PerformanceMetricsTests(unittest.TestCase):
    def test_throughput_uses_whole_operation_elapsed_time(self):
        output = io.StringIO()
        with redirect_stdout(output), patch("workbench_performance_metrics.time.monotonic", return_value=110):
            result = record_performance(
                self, operation="burst_create", measurement="throughput", started_at=100,
                budget_seconds=15, items=500,
            )
        self.assertEqual(50, result["atoms_per_second"])
        self.assertEqual(10, result["elapsed_seconds"])
        self.assertEqual(500, result["items"])
        self.assertEqual(result, json.loads(output.getvalue().removeprefix("WORKBENCH_PERFORMANCE ")))

    def test_latency_violation_fails_even_when_rounded_output_equals_limit(self):
        output = io.StringIO()
        with redirect_stdout(output), patch("workbench_performance_metrics.time.monotonic", return_value=1.50000001):
            with self.assertRaisesRegex(AssertionError, "single_edit"):
                record_performance(
                    self, operation="single_edit", measurement="latency", started_at=0,
                    budget_seconds=1.5,
                )
        self.assertEqual(1.5, json.loads(output.getvalue().removeprefix("WORKBENCH_PERFORMANCE "))["elapsed_seconds"])

    def test_instrumented_runs_cannot_pass_as_acceptance_timings(self):
        for target, value in (("tracemalloc.is_tracing", True), ("sys.getprofile", object())):
            with self.subTest(target=target), redirect_stdout(io.StringIO()):
                with patch("workbench_performance_metrics.time.monotonic", return_value=1), patch(
                    "workbench_performance_metrics." + target, return_value=value,
                ):
                    with self.assertRaisesRegex(AssertionError, "profiling must be disabled"):
                        record_performance(
                            self, operation="single_edit", measurement="latency", started_at=0,
                            budget_seconds=1.5,
                        )

    def test_cold_rebuild_regression_reports_before_failing(self):
        output = io.StringIO()
        with redirect_stdout(output), patch("workbench_performance_metrics.time.monotonic", return_value=31):
            with self.assertRaisesRegex(AssertionError, "cold_index"):
                record_performance(
                    self, operation="cold_index", measurement="cold_rebuild", started_at=0,
                    budget_seconds=30,
                )
        self.assertEqual(31, json.loads(output.getvalue().removeprefix("WORKBENCH_PERFORMANCE "))["elapsed_seconds"])


if __name__ == "__main__":
    unittest.main()
