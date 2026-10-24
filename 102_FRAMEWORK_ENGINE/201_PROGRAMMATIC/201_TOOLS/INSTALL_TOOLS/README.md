# CAPRMEDIO installation

Use one installer with two separate scopes. Both commands are dry-runs unless
`--apply` is supplied. Run with the selected uv-managed environment:

```sh
.caprmedio_runtime/launcher-venv/bin/python -B \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/INSTALL_TOOLS/install.py runtime \
  --harness=codex --projects-root=/Users/am/Documents/My_Repos

.caprmedio_runtime/launcher-venv/bin/python -B \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/INSTALL_TOOLS/install.py project \
  --project-root=/absolute/path/to/project --prefix=MYAPP
```

## Runtime: once per host

`runtime` saves host settings outside all Projects at
`$XDG_CONFIG_HOME/caprmedio/runtime.toml` (default `~/.config/caprmedio/runtime.toml`).
`--host-settings` selects another host carrier. `--projects-root`, `--http-port`
and `--max-loaded-projects` set the shared Docker parameters. Omitted values
retain existing settings; a new carrier requires a repositories folder and
defaults to port `8092` and two warm Project contexts.
Changing host settings requires a coordinated runtime restart; configure-only
installation does not restart a running server.

`--harness=codex` installs the thin Project-context hook and its isolated host
Python environment under `$XDG_DATA_HOME/caprmedio/runtime` (default
`~/.local/share/caprmedio/runtime`). Override this with `--runtime-root`.
It registers one global hook and the shared loopback MCP URL in `CODEX_HOME`
(default `~/.codex`), preserving unrelated configuration. A conflicting existing
CAPRMEDIO MCP connection is refused rather than silently replaced. Review the
hook with `/hooks`; installation does not grant trust or prove activation.
Enable the hook only against the shared MCP contract accepting `project_root`,
not the legacy one-Project server. The installing environment needs the existing
locked `connector-toml` dependency group; the installed hook itself is stdlib-only.

The hook sends the session's full `cwd` as outer `project_root`, preserving native
arguments. A conflicting explicit root refuses the request. The server retains
Project admission and filesystem-boundary validation.

Without `--image`, runtime installation only configures the host and adapter;
it does not call Docker or claim that a server is running. To explicitly start
the shared container, add an already-built/admitted immutable
`--image=sha256:<64-lowercase-hex-digits>` and `--apply`. This delegates to the
existing shared launcher and its bounded image/mount/readiness checks. It does
not build, release, prune images or stop another runtime. The Framework
distribution and complete managed release both include the shared Compose
launcher and canonical thin Skill; minimal legacy Tool-only packages do not.

## Project: once per Project

`project` configures only the selected existing directory. A new Project requires
an explicit `--prefix`; an existing Project retains its declared prefix, control
root, settings and structure. Setup installs the thin `ca` Skill under
`.agents/skills/ca`. `--source-root` may select the Framework distribution that
contains the canonical Skill.

Project setup does not start Docker, configure a global MCP connection, install
global hooks, initialize Git, copy Tool implementations, or invent Scope Units
and Atoms. Existing unrelated files remain untouched; conflicting managed
carriers are refused before effects.

## Existing Tool-package installation

`install_tools.py --repository <root> run` remains the separate legacy managed
Tool-package interface. Its existing `--apply`/`--without-hooks` behavior is unchanged. It is
not the new Project setup command; do not use it to provision the shared host.
