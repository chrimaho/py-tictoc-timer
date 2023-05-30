# Python StdLib Imports
from time import sleep
from unittest import TestCase

# Python Open Source Imports
import pytest

# Local Module Imports
from py_tictoc_timer.tictoc import TicToc


class TestTicToc(TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_tictoc_basic(self):
        with TicToc():
            sleep(1.1)
        captured = self.capsys.readouterr()
        self.assertEqual("Elapsed time: 1secs\n", captured.out)

    def test_tictoc_message(self):
        with TicToc(end_message="Total time:    "):
            sleep(1.1)
        captured = self.capsys.readouterr()
        self.assertEqual("Total time: 1secs\n", captured.out)

    def test_tictoc_advanced(self):
        with TicToc("end", "start"):
            sleep(1.1)
        captured = self.capsys.readouterr()
        self.assertEqual("start\nend: 1secs\n", captured.out)

    def test_tictoc_manual(self):
        tt = TicToc()
        tt.tic()
        sleep(1.1)
        tt.toc()
        captured = self.capsys.readouterr()
        self.assertEqual("Elapsed time: 1secs\n", captured.out)
        self.assertEqual("Time: 1secs", tt.elapsed_str("Time:"))

    def test_tictoc_restart(self):
        tt = TicToc()
        tt.tick()
        sleep(1.1)
        tt.toc(restart=True)
        sleep(1.1)
        tt.tock(restart=True)
        sleep(1.1)
        tt.rtoc()
        sleep(1.1)
        tt.toc()
        captured = self.capsys.readouterr()
        self.assertEqual(
            "Elapsed time: 1secs\nElapsed time: 1secs\nElapsed time: 1secs\nElapsed time: 1secs\n",
            captured.out,
        )
        tt.tic(restart=True)
        sleep(1.1)
        tt.toc()
        sleep(1.1)
        tt.toc()
        captured = self.capsys.readouterr()
        self.assertEqual("Elapsed time: 1secs\nElapsed time: 1secs\n", captured.out)

    def test_tictoc_value(self):
        tt = TicToc()
        tt.tic()
        sleep(1.1)
        val = tt.toc_value(restart=True)
        self.assertBetween(val, 1, 1.5)
        sleep(75.1)
        val = tt.toc_value()
        self.assertBetween(val, 75, 75.5)

    def test_tictoc_string(self):
        tt = TicToc()
        tt.tic()
        sleep(1.1)
        val = tt.toc_string()
        self.assertEqual(val, "1secs")

    def test_tictoc_extended(self):
        with TicToc():
            sleep(75.1)
        captured = self.capsys.readouterr()
        self.assertEqual("Elapsed time: 1mins 15secs\n", captured.out)

    def test_tictoc_raises(self):
        tt = TicToc()
        print(tt.start)
        with self.assertRaises(AttributeError):
            tt.toc()

    def assertBetween(
        self, value: float, lower_limit: float, upper_limit: float
    ) -> bool:
        self.assertTrue(
            lower_limit <= value <= upper_limit,
            msg=f"{value} is not between {lower_limit} and {upper_limit}.",
        )
