"""Fresh definition observations, pinned only for one selected admission."""

from pathlib import Path
import re

from atom_operations import frontmatter_scalar, split_frontmatter
from connector_bindings import FileSource, capture_source


class CurrentDefinitionSources:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.sources: dict[str, FileSource] = {}
        self.identities: dict[str, str] = {}

    def read(
        self, atom_id: str, reference: str, expected_type: str | None = None
    ) -> dict[str, object]:
        if any(
            part in {"archive", "archived", "draft", "drafts"} for part in Path(reference).parts
        ):
            raise ValueError("definition is not a current original Carrier")
        if atom_id in self.identities and self.identities[atom_id] != reference:
            raise ValueError("definition identity has competing source paths")
        source = self.sources.get(reference)
        if source is None:
            source = capture_source(self.root, reference)
            self.sources[reference] = source
        frontmatter, _ = split_frontmatter(source.read_bytes().decode("utf-8"))
        actual_id = frontmatter_scalar(frontmatter, "atom_id")
        version = frontmatter_scalar(frontmatter, "version")
        role, kind = (frontmatter_scalar(frontmatter, field) for field in ("content_role", "type"))
        status = frontmatter_scalar(frontmatter, "status")
        allowed = {
            "CA-O": ("Operations", {"Workflow", "Step", "Action"}),
            "CA-P": ("Plan", {"Plan"}),
            "CA-A": ("Analysis", {"Analysis Report"}),
        }
        required_role, kinds = allowed.get(atom_id.rsplit("-", 1)[0], (None, set()))
        if (
            actual_id != atom_id
            or not isinstance(version, str)
            or re.fullmatch(r"[1-9][0-9]*", version) is None
            or role != required_role
            or kind not in kinds
            or status != ("Done" if role == "Plan" else "Active")
            or (expected_type is not None and kind != expected_type)
        ):
            raise ValueError("current definition identity, role, type or Version is invalid")
        self.identities[atom_id] = reference
        return {
            "atom_id": atom_id,
            "version": int(version),
            "source_path": reference,
            "digest": source.sha256,
        }

    def revalidate(self) -> None:
        for source in self.sources.values():
            source.revalidate()
