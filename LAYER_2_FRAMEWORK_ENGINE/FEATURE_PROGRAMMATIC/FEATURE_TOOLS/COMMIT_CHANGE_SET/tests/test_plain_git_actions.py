"""Git target/data checks remain independent of Journal history."""

import unittest
from unittest import mock

from commit_change_set_fixture import CommitChangeSetTests, commit_change_set as tool


class PlainGitActionsTests(unittest.TestCase):
    def setUp(self):
        self.case = CommitChangeSetTests()
        self.case.setUp()
        self.addCleanup(self.case.tearDown)
        self.root = self.case.root

    def commit_action(self, before, after, action):
        context = tool.gather_context(self.root, self.case.trigger(before, after))
        self.assertEqual(context["action_type"], action)
        result = tool.run(self.root, {"context": context}, apply=True)
        self.assertEqual(self.case.git("rev-parse", "HEAD").strip(), result["commit"])
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        return context

    def test_add_without_journal(self):
        target = "new.txt"
        (self.root / target).write_text("new actual file\n")
        self.commit_action(None, target, "ADD")
        self.assertEqual(self.case.git("show", f"HEAD:{target}"), "new actual file\n")

    def test_move_without_journal(self):
        self.case.git("checkout", "--", self.case.subject)
        moved = self.case.subject.replace("/04_requirement/", "/moved/")
        (self.root / moved).parent.mkdir()
        (self.root / self.case.subject).rename(self.root / moved)
        self.commit_action(self.case.subject, moved, "MOVE")
        self.assertEqual(self.case.git("ls-files", self.case.subject), "")
        self.assertTrue(self.case.git("ls-files", moved).strip())

    def test_move_update_without_journal(self):
        moved = self.case.subject.replace("/04_requirement/", "/moved/")
        (self.root / moved).parent.mkdir()
        (self.root / self.case.subject).rename(self.root / moved)
        self.commit_action(self.case.subject, moved, "MOVE+UPDATE")
        self.assertIn("second", self.case.git("show", f"HEAD:{moved}"))

    def test_remove_without_journal(self):
        (self.root / self.case.subject).unlink()
        self.commit_action(self.case.subject, None, "REMOVE")
        self.assertEqual(self.case.git("ls-files", self.case.subject), "")

    def test_folder_preserves_unchanged_members(self):
        directory = self.root / "docs"
        directory.mkdir()
        (directory / "keep.txt").write_text("unchanged\n")
        (directory / "edit.txt").write_text("before\n")
        self.case.git("add", "docs")
        self.case.git("commit", "-qm", "folder fixture")
        (directory / "edit.txt").write_text("after\n")
        self.commit_action("docs", "docs", "UPDATE")
        self.assertEqual(self.case.git("show", "HEAD:docs/keep.txt"), "unchanged\n")
        self.assertEqual(
            self.case.git("show", "--format=", "--name-only", "HEAD").strip(), "docs/edit.txt"
        )

    def test_source_drift_during_staging_refuses_before_commit(self):
        context = tool.gather_context(self.root, self.case.trigger())
        before = self.case.git("rev-parse", "HEAD")
        original = tool._git

        def mutate_after_add(root, *arguments, **kwargs):
            result = original(root, *arguments, **kwargs)
            if arguments[:1] == ("add",):
                with (root / self.case.subject).open("ab") as stream:
                    stream.write(b"drift\n")
            return result

        with mock.patch.object(tool, "_git", side_effect=mutate_after_add):
            with self.assertRaises(tool.ToolError) as raised:
                tool.run(self.root, {"context": context}, apply=True)
        self.assertEqual(raised.exception.code, "stale-context")
        self.assertEqual(self.case.git("rev-parse", "HEAD"), before)
        self.assertEqual(self.case.git("diff", "--cached", "--name-only"), "")


if __name__ == "__main__":
    unittest.main()
