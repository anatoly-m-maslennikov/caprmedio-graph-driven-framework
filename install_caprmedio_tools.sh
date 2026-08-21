#!/bin/sh
set -eu

repository=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
installed="$repository/.caprmedio_install/bin/install-tools"
canonical="$repository/102_FRAMEWORK_ENGINE/TOOLS/INSTALL_TOOLS/install_tools.py"

if [ -x "$installed" ]; then
    "$installed" run --apply
elif [ -f "$canonical" ]; then
    PYTHONDONTWRITEBYTECODE=1 python3 -B "$canonical" --repository "$repository" run --apply
else
    printf '%s\n' "CAPRMEDIO installer not found in $repository" >&2
    exit 1
fi

"$repository/.caprmedio_install/bin/install-tools" status
