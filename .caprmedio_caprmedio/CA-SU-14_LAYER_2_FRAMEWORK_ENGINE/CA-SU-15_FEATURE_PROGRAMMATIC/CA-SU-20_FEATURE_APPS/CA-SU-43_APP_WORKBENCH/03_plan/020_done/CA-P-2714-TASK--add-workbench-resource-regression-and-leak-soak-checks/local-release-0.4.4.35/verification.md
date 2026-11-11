# Local release verification

Version 0.4.4.35 is installed and running. The Operator selected Workbench and query_run and explicitly excluded unrelated tool failures. All 105 selected Workbench tests passed with zero skips. The health endpoint is ready; Workbench HTML and both referenced JS/CSS assets load. HTTP query_run returned three real Current Atoms; MCP query_run returned three real Atoms and a native count query returned 5,492 indexed Atoms. No query was saved and no source Atom was mutated by the smoke checks.

The running image is sha256:34ef7e3b2234ef48d4c08578a1db74d7fcd3c292a93a6eb9b842cdda412ad759, capped at one CPU and 1,536 MiB. Installed source_reader.py, source_watcher.py and incremental_relations.py match the tested checkout byte for byte.

The local-release result is completed_with_cleanup_pending: the prior Project container and proven-owned old image were removed, while one older image with unproven Project ownership was retained. No unrelated tools were repaired or claimed verified; no full-suite-green claim is made.
