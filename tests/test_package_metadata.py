from pathlib import Path
import unittest


class PackageMetadataTests(unittest.TestCase):
    def test_runtime_dependencies_pin_requests_last(self):
        pyproject = Path("pyproject.toml").read_text()
        dependency_block = pyproject.split("dependencies = [", 1)[1].split("]", 1)[0]
        dependencies = [
            line.strip().rstrip(",").strip('"')
            for line in dependency_block.splitlines()
            if line.strip()
        ]

        self.assertEqual(dependencies[-1], "requests==2.25.1")

    def test_generated_requirements_include_requests_pin(self):
        requirements = Path("src/tricahue.egg-info/requires.txt").read_text().splitlines()
        runtime_requirements = requirements[: requirements.index("")]

        self.assertEqual(runtime_requirements[-1], "requests==2.25.1")


if __name__ == "__main__":
    unittest.main()
