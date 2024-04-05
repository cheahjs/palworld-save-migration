import contextlib
import os
import subprocess
import unittest

from parameterized import parameterized


class TestCliScripts(unittest.TestCase):
    @parameterized.expand(
        [
            ("Level.sav"),
            ("Level-tricky-unicode-player-name.sav"),
            ("LevelMeta.sav"),
            ("LocalData.sav"),
            ("WorldOption.sav"),
            ("00000000000000000000000000000001.sav"),
            ("unicode-saves/Level.sav"),
            ("unicode-saves/LevelMeta.sav"),
            ("unicode-saves/LocalData.sav"),
            ("unicode-saves/WorldOption.sav"),
            ("unicode-saves/00000000000000000000000000000001.sav"),
            ("larger-saves/Level.sav"),
            ("larger-saves/LocalData.sav"),
            ("larger-saves/00000000000000000000000000000001.sav"),
            ("v0.2.0.6/Level.sav"),
        ]
    )
    def test_sav_roundtrip(self, file_name):
        try:
            base_name = os.path.basename(file_name)
            dir_name = os.path.dirname(file_name)
            # Convert sav to JSON
            run = subprocess.run(
                [
                    "python3",
                    "-m",
                    "palworld_save_tools.commands.convert",
                    f"tests/testdata/{dir_name}/{base_name}",
                ]
            )
            self.assertEqual(run.returncode, 0)
            self.assertTrue(
                os.path.exists(f"tests/testdata/{dir_name}/{base_name}.json")
            )
            # Convert JSON back to sav
            os.rename(
                f"tests/testdata/{dir_name}/{base_name}.json",
                f"tests/testdata/{dir_name}/1-{base_name}.json",
            )
            run = subprocess.run(
                [
                    "python3",
                    "-m",
                    "palworld_save_tools.commands.convert",
                    f"tests/testdata/{dir_name}/1-{base_name}.json",
                ]
            )
            self.assertEqual(run.returncode, 0)
            self.assertTrue(os.path.exists(f"tests/testdata/{dir_name}/1-{base_name}"))
            # Reconvert sav back to JSON
            os.rename(
                f"tests/testdata/{dir_name}/1-{base_name}",
                f"tests/testdata/{dir_name}/2-{base_name}",
            )
            run = subprocess.run(
                [
                    "python3",
                    "-m",
                    "palworld_save_tools.commands.convert",
                    f"tests/testdata/{dir_name}/2-{base_name}",
                ]
            )
            self.assertEqual(run.returncode, 0)
            self.assertTrue(
                os.path.exists(f"tests/testdata/{dir_name}/2-{base_name}.json")
            )
            # Reconvert JSON back to sav
            os.rename(
                f"tests/testdata/{dir_name}/2-{base_name}.json",
                f"tests/testdata/{dir_name}/3-{base_name}.json",
            )
            run = subprocess.run(
                [
                    "python3",
                    "-m",
                    "palworld_save_tools.commands.convert",
                    f"tests/testdata/{dir_name}/3-{base_name}.json",
                ]
            )
            self.assertEqual(run.returncode, 0)
            self.assertTrue(os.path.exists(f"tests/testdata/{dir_name}/3-{base_name}"))
            # Compare the final sav to the intermediate save
            with open(f"tests/testdata/{dir_name}/2-{base_name}", "rb") as f:
                intermediate_data = f.read()
            with open(f"tests/testdata/{dir_name}/3-{base_name}", "rb") as f:
                final_data = f.read()
            self.assertEqual(intermediate_data, final_data)
        finally:
            with contextlib.suppress(FileNotFoundError):
                os.remove(f"tests/testdata/{dir_name}/{base_name}.json")
            with contextlib.suppress(FileNotFoundError):
                os.remove(f"tests/testdata/{dir_name}/1-{base_name}")
            with contextlib.suppress(FileNotFoundError):
                os.remove(f"tests/testdata/{dir_name}/1-{base_name}.json")
            with contextlib.suppress(FileNotFoundError):
                os.remove(f"tests/testdata/{dir_name}/2-{base_name}")
            with contextlib.suppress(FileNotFoundError):
                os.remove(f"tests/testdata/{dir_name}/2-{base_name}.json")
            with contextlib.suppress(FileNotFoundError):
                os.remove(f"tests/testdata/{dir_name}/3-{base_name}")
            with contextlib.suppress(FileNotFoundError):
                os.remove(f"tests/testdata/{dir_name}/3-{base_name}.json")
