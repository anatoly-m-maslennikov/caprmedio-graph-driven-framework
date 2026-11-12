# CA-R-1525@25
# CA-M-399@20

"""Project Journal observations for the Change Current Status Workflow."""

from datetime import UTC, datetime
from itertools import groupby
from uuid import uuid4

from work_journal import append_sealed_events


_AUTHOR = 'atom-lifecycle'


def _error_references(errors):
    return [{key: error[key] for key in ('code', 'field') if key in error} for error in errors]


class StatusRunJournal:
    def __init__(self, selection, binding, source_sha256):
        self.selection = selection
        self.run_id = str(uuid4())
        self.binding = dict(binding)
        self.source_sha256 = dict(source_sha256)
        self._observations = []

    def _record(self, event, outcome, **details):
        self._observations.append({
            'schema_version': 4,
            'kind': 'workflow_execution',
            'event_id': str(uuid4()),
            'action_id': self.run_id,
            'event': event,
            'author': _AUTHOR,
            'occurred_at': datetime.now(UTC).isoformat(),
            'workflow_run_id': self.run_id,
            'workflow_binding': self.binding,
            'source_sha256': self.source_sha256,
            'outcome': outcome,
            **details,
        })

    def started(self):
        if not self._observations:
            self._record('workflow_started', 'started')

    def step(self, entry):
        step_run_id = str(uuid4())
        outcome = entry['outcome']
        self._record(f'step_{outcome}', outcome, step_run_id=step_run_id, step=entry['step'],
                     action=entry['action'], target=entry['target'], effects=entry['effects'],
                     errors=_error_references(entry['errors']))
        return step_run_id

    def finish(self, outcome, errors):
        if not self._observations:
            return []
        self._record(f'workflow_{outcome}', outcome, errors=_error_references(errors))
        observations, self._observations = self._observations, []
        try:
            self.selection._revalidate_boundary()
            for date, events in groupby(observations, key=lambda event: event['occurred_at'][:10]):
                append_sealed_events(self.selection.root, list(events), author=_AUTHOR, local_date=date,
                                     timezone='UTC', control_root=self.selection.control_relative)
        except (OSError, RuntimeError, ValueError):
            return [{'code': 'journal_append_failed',
                     'message': 'Could not confirm all Workflow observations were appended to the Project Journal.'}]
        return []
