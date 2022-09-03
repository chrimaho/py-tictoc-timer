from time import sleep
from unittest import TestCase
import sys
import pytest

from py_tictoc.tictoc import TicToc


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
        tt.tic()
        sleep(1.1)
        tt.toc(restart=True)
        sleep(1.1)
        tt.rtoc()
        sleep(1.1)
        tt.toc()
        captured = self.capsys.readouterr()
        self.assertEqual(
            "Elapsed time: 1secs\nElapsed time: 1secs\nElapsed time: 1secs\n",
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
        val = tt.toc_value()
        sys.stdout.write(f"{val}")
        self.assertGreaterEqual(val, 1)
        self.assertLessEqual(val, 1.5)

    def test_tictoc_extended(self):
        with TicToc():
            sleep(75.1)
        captured = self.capsys.readouterr()
        self.assertEqual("Elapsed time: 1mins 15secs\n", captured.out)
