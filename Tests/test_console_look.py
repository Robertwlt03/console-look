"""Tests the Python half of console-look.

Start:  PYTHONPATH=src python3 -m unittest discover -s Tests
Needs:  Python 3.13 or newer
"""

import io
import os
import unittest
from contextlib import redirect_stdout

import console_look


def printed(piece, *arguments) -> str:
    with redirect_stdout(io.StringIO()) as output:
        piece(*arguments)
    return output.getvalue()


class ConsoleLookTests(unittest.TestCase):
    def setUp(self) -> None:
        for name in (console_look.HEADED_VARIABLE, console_look.STEP_VARIABLE):
            os.environ.pop(name, None)

    def test_frame_lines_line_up(self) -> None:
        lines = printed(console_look.frame, "Built", ["build/App", "a longer detail"],
                        console_look.SUCCESS).splitlines()
        widths = {console_look.visible_length(line) for line in lines if line}
        self.assertEqual(len(widths), 1)

    def test_frame_as_a_step_is_one_line(self) -> None:
        os.environ[console_look.STEP_VARIABLE] = "1"
        lines = printed(console_look.frame, "Built", ["build/App"], console_look.SUCCESS)
        self.assertEqual(len(lines.splitlines()), 1)
        self.assertIn("Built", lines)

    def test_heading_shows_once(self) -> None:
        self.assertIn("Build", printed(console_look.heading, "Build"))
        self.assertEqual(printed(console_look.heading, "Build again"), "")

    def test_missing_command_fails_without_traceback(self) -> None:
        with redirect_stdout(io.StringIO()) as output:
            status = console_look.main(["wait", "Compiling", "no-such-command-anywhere"])
        self.assertEqual(status, console_look.NOT_STARTED)
        self.assertIn(console_look.FAILED_MARK, output.getvalue())

    def test_empty_lists_are_refused(self) -> None:
        with self.assertRaises(ValueError):
            console_look.ask_choice("Pick one", [])
        with self.assertRaises(ValueError):
            console_look.wait("Nothing", [])

    def test_stopped_takes_text_alone(self) -> None:
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(console_look.main(["stopped", "Build failed"]), 0)
        self.assertIn("Build failed", output.getvalue())
        self.assertNotIn("Unknown piece", output.getvalue())

    def test_unknown_piece_fails(self) -> None:
        with redirect_stdout(io.StringIO()):
            self.assertEqual(console_look.main(["nothing"]), console_look.UNKNOWN_PIECE)


if __name__ == "__main__":
    unittest.main()
