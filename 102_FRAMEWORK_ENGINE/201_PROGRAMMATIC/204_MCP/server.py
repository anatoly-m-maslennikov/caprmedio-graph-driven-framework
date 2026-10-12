"""Stable stdio gateway entry point, with an explicit Streamable HTTP mode."""
import argparse
import asyncio
from pathlib import Path
from hot_reload import Gateway, startup_selection, bind_selection

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True, type=Path)
    parser.add_argument('--control-root')
    parser.add_argument('--instance-id')
    parser.add_argument('--host-project-root')
    parser.add_argument('--transport', choices=('stdio', 'streamable-http'), default='stdio')
    args = parser.parse_args()
    if args.transport == 'stdio':
        selection = startup_selection(args.project_root, args.control_root, args.instance_id, args.host_project_root)
        with bind_selection(selection):
            asyncio.run(Gateway(args.project_root, selection=selection).serve())
    else:
        from http_server import main as serve_http
        import sys
        sys.argv = [sys.argv[0], '--project-root', str(args.project_root)]
        for flag, value in (('--control-root', args.control_root), ('--instance-id', args.instance_id),
                            ('--host-project-root', args.host_project_root)):
            if value is not None:
                sys.argv += [flag, value]
        serve_http()
