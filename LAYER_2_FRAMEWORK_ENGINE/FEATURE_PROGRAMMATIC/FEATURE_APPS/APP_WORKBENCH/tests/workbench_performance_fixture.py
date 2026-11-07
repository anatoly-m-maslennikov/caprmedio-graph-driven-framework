# CA-E-677@16
# CA-E-780@7
"""Representative disposable sources for the Workbench performance gates."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import random

from scope_declaration_render import render_scope_declaration
from scope_declaration_test_support import write_scope_unit_declarations
from smalltest_support import source_path, write_settings


FIXTURE_ATOM_COUNT = 5_000
BATCH_COUNT = 500
BASE_REFERENCE = "CA-R-900000"
RELATION_REFERENCE = "CA-R-900001"
CONTENT_MODEL_REFERENCE = "CA-R-900002"
BATCH_PREFIX = "CA-R-200"
SOURCE_SCOPE = "PERF_SOURCE"
TARGET_SCOPE = "PERF_TARGET"
RENAMED_TARGET_SCOPE = "PERF_TARGET_RENAMED"
RELATION_TYPES = (
    "IS_CONTAINED_BY",
    "CONTAINS",
    "IS_BLOCKED_BY",
    "BLOCKS",
)


def batch_ids() -> frozenset[str]:
    return frozenset(f"{BATCH_PREFIX}{index:03d}" for index in range(BATCH_COUNT))


def _details(atom_id: str, version: int, *, changed: bool) -> str:
    randomizer = random.Random(f"workbench-performance:{atom_id}:{version}")
    topics = ("traceability", "indexing", "relation projection", "carrier structure")
    sentences = [
        f"{atom_id} represents {randomizer.choice(topics)} in a representative project.",
        "Its Claim is intentionally ordinary source content, not synthetic empty metadata.",
        "The indexed Header and relation values stay predictable for the test oracle.",
        f"The required outcome code is {version}.",
    ]
    if changed:
        sentences.append("This version records a real content update for delta indexing.")
    filler = " ".join(sentences)
    return (
        "## Summary\n\n"
        f"Index representative Atom {atom_id}.\n\n"
        "## Claim\n\n### Prose Claim\n\n"
        + filler
        + "\n\n## Details\n\n"
        + (filler + " ") * 7
        + "\n"
    )


def _header(
    atom_id: str,
    *,
    version: int,
    scope_id: str,
    scope_name: str,
    destination: str,
    relation_target: str | None,
    form: str = "Definition",
) -> str:
    randomizer = random.Random(f"workbench-header:{atom_id}")
    label = f"fixture-{randomizer.randrange(1_000_000):06d}"
    topics = ("Subject/Graph/Node/Project Model/Atom", "Subject/Graph/Relation")
    relation = "{}" if relation_target is None else f"{{IS_BLOCKED_BY: '{relation_target}'}}"
    return (
        "---\n"
        "identity:\n"
        f"  atom_id: {atom_id}\n"
        f"  ref_id: {atom_id}\n"
        "context:\n"
        "  container:\n"
        f"    scope_unit: {scope_id}\n"
        "  role: Requirement\n"
        f"  form: {form}\n"
        f"  label: {label}\n"
        f"  tier: {randomizer.randrange(1, 5)}\n"
        f"  scope_unit_name: {scope_name}\n"
        "  topics:\n"
        f"    main_subject: {randomizer.choice(topics)}\n"
        "    dependencies: []\n"
        f"relations: {relation}\n"
        "state:\n"
        "  status: Active\n"
        f"  version: {version}\n"
        f"  updated_at: '2026-11-07 00:{randomizer.randrange(60):02d}:00 +0000'\n"
        "destination:\n"
        "  file:\n"
        f"    name: {Path(destination).name}\n"
        f"    path: {Path(destination).parent.as_posix()}\n"
        "---\n"
    )


def _relation_header(destination: str) -> str:
    subjects = "\n".join(f"    - Subject/Graph/Relation//{name}" for name in RELATION_TYPES)
    return (
        "---\n"
        "identity:\n"
        f"  atom_id: {RELATION_REFERENCE}\n"
        f"  ref_id: {RELATION_REFERENCE}\n"
        "context:\n"
        "  container:\n"
        "    scope_unit: TEST-SU-1\n"
        "  role: Requirement\n"
        "  form: Relation Definition\n"
        "  tier: 1\n"
        "  topics:\n"
        "    main_subject:\n"
        f"{subjects}\n"
        "    dependencies: []\n"
        "relations: {}\n"
        "state:\n"
        "  status: Active\n"
        "  version: 1\n"
        "  updated_at: '2026-11-07 00:00:00 +0000'\n"
        "destination:\n"
        "  file:\n"
        f"    name: {Path(destination).name}\n"
        f"    path: {destination}\n"
        "---\n"
    )


@dataclass
class PerformanceFixture:
    root: Path
    control: Path
    declarations: dict[str, dict[str, object]]
    source_directory: Path
    target_directory: Path
    staging_directory: Path
    batch_directory: Path

    @property
    def source_scope_id(self) -> str:
        return str(self.declarations[SOURCE_SCOPE]["scope_id"])

    @property
    def target_scope_id(self) -> str:
        target = self.declarations.get(TARGET_SCOPE) or self.declarations[RENAMED_TARGET_SCOPE]
        return str(target["scope_id"])

    def relative(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def write_atom(
        self,
        path: Path,
        atom_id: str,
        *,
        version: int,
        scope_id: str,
        scope_name: str,
        changed: bool = False,
        relation_target: str | None = BASE_REFERENCE,
        destination: str | None = None,
        body: str | None = None,
    ) -> None:
        destination = destination or (
            self.relative(path) if path.is_relative_to(self.root) else path.name
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            _header(
                atom_id,
                version=version,
                scope_id=scope_id,
                scope_name=scope_name,
                destination=destination,
                relation_target=relation_target,
            )
            + (body if body is not None else _details(atom_id, version, changed=changed)),
            encoding="utf-8",
        )

    def rewrite_batch(
        self,
        *,
        version: int,
        scope_id: str,
        scope_name: str,
        changed: bool = False,
        preserve_content: bool = False,
    ) -> None:
        for atom_id in sorted(batch_ids()):
            path = next(self.batch_directory.glob(f"{atom_id}-*.md"))
            existing = (
                path.read_text(encoding="utf-8").split("---", 2)[2] if preserve_content else None
            )
            self.write_atom(
                path,
                atom_id,
                version=version,
                scope_id=scope_id,
                scope_name=scope_name,
                changed=changed,
                body=existing,
            )

    def rename_batch_files(self, *, version: int, suffix: str, changed: bool) -> None:
        renamed = []
        for atom_id in sorted(batch_ids()):
            old_path = next(self.batch_directory.glob(f"{atom_id}-*.md"))
            new_path = old_path.with_name(f"{atom_id}-{suffix}.md")
            old_path.rename(new_path)
            renamed.append((atom_id, new_path))
        for atom_id, path in renamed:
            self.write_atom(
                path,
                atom_id,
                version=version,
                scope_id=self.source_scope_id,
                scope_name=SOURCE_SCOPE,
                changed=changed,
                body=path.read_text(encoding="utf-8").split("---", 2)[2] if not changed else None,
            )

    def move_batch_to_target(self, *, version: int) -> None:
        target = self.target_directory / self.batch_directory.name
        target.parent.mkdir(parents=True, exist_ok=True)
        self.batch_directory.rename(target)
        self.batch_directory = target
        self.rewrite_batch(
            version=version,
            scope_id=self.target_scope_id,
            scope_name=TARGET_SCOPE,
            preserve_content=True,
        )

    def rename_target_scope(self, *, version: int) -> None:
        old_target = self.declarations[TARGET_SCOPE]
        old_authority = Path(old_target["authority_path"])
        new_authority = old_authority.with_name(
            old_authority.name.replace(TARGET_SCOPE, RENAMED_TARGET_SCOPE)
        )
        old_delivery = Path(old_target["delivery_path"])
        new_delivery = old_delivery.with_name(
            old_delivery.name.replace(TARGET_SCOPE, RENAMED_TARGET_SCOPE)
        )
        declaration_path = Path(old_target["declaration_path"])
        project_name = next(name for name, row in self.declarations.items() if row["project"])
        replacement = self.root.parent / f"{declaration_path.name}.replacement"
        replacement.write_text(
            render_scope_declaration(
                name=RENAMED_TARGET_SCOPE,
                project_name=project_name,
                atom_id=str(old_target["atom_id"]),
                updated_at="2026-11-07 00:00:00 +0000",
                scope_id=str(old_target["scope_id"]),
                label=old_target["scope_unit_label"],
                ordered=bool(old_target["ordered"]),
                order_number=old_target["local_order"],
                parent=str(old_target["parent"]),
                project=False,
            ),
            encoding="utf-8",
        )
        replacement.replace(declaration_path)
        old_authority.rename(new_authority)
        renamed_target = {
            **old_target,
            "scope_unit_name": RENAMED_TARGET_SCOPE,
            "authority_path": new_authority,
            "delivery_path": new_delivery,
        }
        self.declarations = {
            name: row for name, row in self.declarations.items() if name != TARGET_SCOPE
        }
        self.declarations[RENAMED_TARGET_SCOPE] = renamed_target
        self.target_directory = source_path(
            self.declarations,
            RENAMED_TARGET_SCOPE,
            "04_requirement",
            "placeholder.md",
        ).parent
        self.batch_directory = self.target_directory / self.batch_directory.name
        self.rewrite_batch(
            version=version,
            scope_id=str(renamed_target["scope_id"]),
            scope_name=RENAMED_TARGET_SCOPE,
            preserve_content=True,
        )


def prepare_fixture(temporary_root: Path) -> PerformanceFixture:
    root = temporary_root / "repository"
    root.mkdir()
    root.chmod(0o755)
    control = write_settings(root)
    rows = (
        {
            "scope_unit_name": SOURCE_SCOPE,
            "scope_unit_type": "Ordered",
            "scope_unit_label": "APP",
            "local_order": 1,
        },
        {
            "scope_unit_name": TARGET_SCOPE,
            "scope_unit_type": "Ordered",
            "scope_unit_label": "APP",
            "local_order": 2,
        },
    )
    declarations = write_scope_unit_declarations(root, rows, control_root=control)
    source_directory = source_path(
        declarations, SOURCE_SCOPE, "04_requirement", "placeholder.md"
    ).parent
    target_directory = source_path(
        declarations, TARGET_SCOPE, "04_requirement", "placeholder.md"
    ).parent
    staging_directory = temporary_root / "staged"
    batch_directory = source_directory / "batch"
    fixture = PerformanceFixture(
        root,
        control,
        declarations,
        source_directory,
        target_directory,
        staging_directory,
        batch_directory,
    )
    relation_path = source_directory / f"{RELATION_REFERENCE}-relations.md"
    relation_path.parent.mkdir(parents=True, exist_ok=True)
    relation_path.write_text(
        _relation_header(fixture.relative(relation_path))
        + "# Summary\n\nDefine representative Relations.\n\n## Claim\n\n```CFEL\n"
        "Relation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;\n"
        "Relation//IS_BLOCKED_BY ((HAS_INVERSE)) Relation//BLOCKS;\n```\n",
        encoding="utf-8",
    )
    model_path = source_directory / f"{CONTENT_MODEL_REFERENCE}-content-model.md"
    model_path.write_text(
        _header(
            CONTENT_MODEL_REFERENCE,
            version=1,
            scope_id=fixture.source_scope_id,
            scope_name=SOURCE_SCOPE,
            destination=fixture.relative(model_path),
            relation_target=None,
            form="Declaration",
        )
        + "# Summary\n\nDefine representative Content.\n\n## Claim\n\n```CFEL\n# model\n"
        "Atom.Content.Summary{::1}:: {::1};\n"
        "Atom/(.Header.Role in RMED).Content.Claim{::1}:: []{::0};\n"
        "Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};\n"
        "Atom/(.Header.Role in RMED).Content.Details{::0..1}:: [string]{::0..1};\n```\n",
        encoding="utf-8",
    )
    fixture.write_atom(
        source_directory / f"{BASE_REFERENCE}-relation-target.md",
        BASE_REFERENCE,
        version=1,
        scope_id=fixture.source_scope_id,
        scope_name=SOURCE_SCOPE,
        relation_target=None,
    )
    declaration_count = len(declarations)
    stable_count = FIXTURE_ATOM_COUNT - declaration_count - 3
    for index in range(stable_count):
        atom_id = f"CA-R-{100_000 + index}"
        fixture.write_atom(
            source_directory / f"{atom_id}-stable.md",
            atom_id,
            version=1,
            scope_id=fixture.source_scope_id,
            scope_name=SOURCE_SCOPE,
        )
    fixture.staging_directory.mkdir()
    for atom_id in sorted(batch_ids()):
        name = f"{atom_id}-created.md"
        fixture.write_atom(
            fixture.staging_directory / name,
            atom_id,
            version=1,
            scope_id=fixture.source_scope_id,
            scope_name=SOURCE_SCOPE,
            destination=fixture.relative(fixture.batch_directory / name),
        )
    return fixture


__all__ = [
    "BASE_REFERENCE",
    "BATCH_COUNT",
    "BATCH_PREFIX",
    "CONTENT_MODEL_REFERENCE",
    "FIXTURE_ATOM_COUNT",
    "PerformanceFixture",
    "RENAMED_TARGET_SCOPE",
    "SOURCE_SCOPE",
    "TARGET_SCOPE",
    "batch_ids",
    "prepare_fixture",
]


def expected_claim(atom_id: str, version: int, *, changed: bool) -> str:
    return (
        _details(atom_id, version, changed=changed)
        .split("### Prose Claim\n\n", 1)[1]
        .split("\n\n## Details", 1)[0]
    )
