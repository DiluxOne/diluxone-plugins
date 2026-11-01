"""The catalog's files and its README agree (#3).

agent-manifests.py catalog (run by `make pre-pr`) checks that every entry
points to a plugin of the ai-agent-plugin kind, each from its own
repository. This checks what a person reads and types: the catalog's name,
the README's install commands for every tool that has a catalog, and the
way out of the old catalogs.
"""
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CENTRAL = os.path.join(ROOT, os.environ.get("DX_CENTRAL") or ".dx-central")
NAME = "diluxone-plugins-ai"
REPO = f"DiluxOne/{NAME}"
CATALOGS = (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json")
# The command that adds a catalog, per tool (tools.yml `how`); a tool the
# organisation gives a catalog that is not here fails the test.
ADD = {
    "claude-code": "/plugin marketplace add",
    "copilot": "copilot plugin marketplace add",
    "codex": "codex plugin marketplace add",
}
# The old catalogs: diluxone/diluxone-plugins, and DAW's own.
OLD = ("diluxone", "dilux")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def catalog_tools():
    """The tools that install from a catalog, from the organisation's
    agent-manifests.py tools (id, manifest, install per line)."""
    script = os.path.join(CENTRAL, "scripts", "agent-manifests.py")
    if not os.path.isfile(script):
        raise unittest.SkipTest(f"{CENTRAL} is not a checkout of DiluxOne/.github")
    out = subprocess.run([sys.executable, "-I", script, "tools"], check=True, capture_output=True, text=True).stdout
    return [line.split("\t")[0] for line in out.splitlines() if line.split("\t")[-1] == "catalog"]


class Catalog(unittest.TestCase):
    def setUp(self):
        self.readme = read("README.md")

    def test_every_catalog_file_is_named_diluxone_plugins_ai(self):
        for path in CATALOGS:
            with self.subTest(path=path):
                self.assertEqual(json.loads(read(path))["name"], NAME)

    def test_the_readme_names_every_plugin_of_every_catalog_file(self):
        for path in CATALOGS:
            for entry in json.loads(read(path))["plugins"]:
                with self.subTest(path=path, plugin=entry["name"]):
                    self.assertIn(f"`{entry['name']}`", self.readme)

    def test_the_readme_installs_each_plugin_from_this_catalog(self):
        for entry in json.loads(read(CATALOGS[0]))["plugins"]:
            with self.subTest(plugin=entry["name"]):
                self.assertIn(f"/plugin install {entry['name']}@{NAME}", self.readme)
                self.assertIn(f"copilot plugin install {entry['name']}@{NAME}", self.readme)

    def test_the_readme_adds_this_catalog_in_every_catalog_tool(self):
        for tool in catalog_tools():
            with self.subTest(tool=tool):
                self.assertIn(tool, ADD, f"{tool} installs from a catalog and the test knows no command that adds one")
                self.assertIn(f"{ADD[tool]} {REPO}", self.readme)

    def test_the_readme_tells_who_added_an_old_catalog_to_move(self):
        for old in OLD:
            with self.subTest(marketplace=old):
                self.assertIn(f"/plugin marketplace remove {old}\n", self.readme)
        self.assertIn("## Moving from the old catalog", self.readme)


if __name__ == "__main__":
    unittest.main()
