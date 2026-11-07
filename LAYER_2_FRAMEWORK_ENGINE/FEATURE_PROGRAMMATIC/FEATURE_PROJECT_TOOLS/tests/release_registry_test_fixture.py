"""Small deterministic generator used by package-release fixtures."""

from pathlib import Path


def write_registry_generator(directory: Path) -> Path:
    script = directory / "generate_tool_registry.py"
    script.write_text(
        "from pathlib import Path\n"
        "import sys\n"
        "root = Path(sys.argv[sys.argv.index('--package-root') + 1])\n"
        "output = root / 'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_registry.json'\n"
        "output.write_text('{\"schema_version\":1,\"providers\":[]}\\n', encoding='utf-8')\n",
        encoding="utf-8",
    )
    return script
