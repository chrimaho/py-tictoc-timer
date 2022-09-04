from __future__ import annotations

from timeit import default_timer
from typing import Optional

from typeguard import typechecked


__all__ = ["TicToc"]
__author__ = "Chris Mahoney"
__version__ = "0.1.13"


class TicToc:
    """
    Summary:
        TicToc Timer to be used similar to MATLAB's `tic` and `toc` functions.

    Attributes:
        start (float):
            The timestamp of when the timer started.
        end (float):
            The timestamp of when the timer ended.
        elapsed (float):
            The duration time of the elapsed time difference between `start` and `end`.
        print_time (bool, optional):
            Whether or not the `elapsed` time should be printed during the `.toc()` method.
            Default: `True`.
        begin_message (Optional[str], optional):
            When executed within a context manager (using the `with` parameter), this is the message that should be printed at the start of the context.
            Default: `None`.
        end_message (Optional[str], optional):
            When executed within a context manager (using the `with` parameter), this is the message that should be printed at the end of the context.
            Default: `"Elapsed time:"`.
        restart (Optional[bool], optional):
            Whether or not the timer should restart again after after the `.toc()` method is called.
            Default: `None`.

    ???+ Info "Credit"
        Inspiration from: https://github.com/ericcfields/pytictoc.

    ???+ Example "Examples"

        Basic execution:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> tt = TicToc()
        >>> tt.tic()
        >>> sleep(1.1)
        >>> tt.toc()
        Elapsed time: 1secs
        ```

        Context manager:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> with TicToc():
        ...     sleep(1.1)
        Elapsed time: 1secs
        ```

        Context manager with custom messages:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> with TicToc(begin_message="start", end_message="end"):
        ...     sleep(1.1)
        start
        end: 1secs
        ```

        Custom message:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> with TicToc("Total Time"):
        ...     sleep(1.1)
        Total time: 1secs
        ```

        With restart during `.tic()`:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> tt = TicToc()
        >>> tt.tic(restart=True)
        >>> sleep(1.1)
        >>> toc()
        Elapsed time: 1secs
        >>> toc()
        Elapsed time: 1secs
        ```

        With restart during `.toc()`:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> tt = TicToc()
        >>> tt.tic()
        >>> sleep(1.1)
        >>> tt.toc(restart=True)
        Elapsed time: 1secs
        >>> tt.toc()
        Elapsed time: 1secs
        ```

        With restart using `.rtoc()`:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> tt = TicToc()
        >>> tt.tic()
        >>> sleep(1.1)
        >>> tt.rtoc()
        Elapsed time: 1secs
        >>> tt.toc()
        Elapsed time: 1secs
        ```

        With time returned:
        ```python linenums="1"
        >>> from tictoc import TicToc
        >>> from time import sleep
        >>> tt = TicToc()
        >>> tt.tic()
        >>> sleep(1.1)
        >>> value = tt.toc_value()
        >>> print(round(value, 1))
        1.1
        ```
    """

    @typechecked
    def __init__(
        self,
        end_message: str = "Elapsed time:",
        begin_message: Optional[str] = None,
        print_time: bool = True,
    ) -> None:
        self.start = float("nan")
        self.end = float("nan")
        self.elapsed = float("nan")
        self.restart: Optional[bool] = None
        self.print_time = print_time
        self.begin_message = begin_message
        self.end_message = self._clean_message(end_message)

    def tic(self, restart: Optional[bool] = None):
        """
        Summary:
            Start the timer.

        Params:
            restart (Optional[bool], optional):
                Whether or not the timer should be restarted when the `.toc()` method is called. Defaults to `None`.
        """
        if restart:
            self.restart = restart
        self.start = default_timer()

    @typechecked
    def toc(
        self,
        msg: Optional[str] = None,
        restart: Optional[bool] = None,
        print_time: Optional[bool] = None,
    ) -> None:
        """
        Summary:
            Stop the timer.

        Params:
            msg (Optional[str], optional):
                The message to be printed at the end of the timer. Defaults to `None`.
            restart (Optional[bool], optional):
                Whether or not the timer should be restarted. Defaults to `None`.
            print_time (Optional[bool], optional):
                Whether or not the elapsed time should be printed. Defaults to `None`.

        Returns:
            type(None):
                Nothing is returned.
        """
        self.end = default_timer()
        self.elapsed = self.end - self.start
        if print_time is None:
            print_time = self.print_time
        if print_time:
            print(self.elapsed_str(msg or self.end_message))
        if restart:
            self.restart = restart
        if self.restart:
            self.start = default_timer()
        return None

    def rtoc(
        self,
        msg: Optional[str] = None,
        print_time: Optional[bool] = None,
    ) -> None:
        """
        Summary:
            Restartable toc.

        Params:
            msg (Optional[str]):
                The message to be printed at the end of the timer. Defaults to `None`.
            print_time (Optional[bool], optional):
                Whether or not the elapsed time should be printed. Defaults to `None`.
        """
        self.toc(msg=msg, restart=True, print_time=print_time)

    @typechecked
    def toc_value(self, restart: bool = False) -> float:
        """
        Summary:
            Stop the timer and return the time value.

        Params:
            restart (bool, optional):
                Whether or not the timer should be restarted. Defaults to `False`.

        Returns:
            float:
                The elapsed time.
        """
        self.toc(restart=restart, print_time=False)
        return self.elapsed

    def __enter__(self) -> None:
        """
        Summary:
            Begin timer within a context manager.
        """
        if self.begin_message:
            print(self.begin_message)
        self.tic()

    def __exit__(self, *args) -> None:
        """
        Summary:
            End timer within a context manager.
        """
        self.toc(msg=self.end_message, restart=False)

    def elapsed_str(self, msg: Optional[str] = None) -> str:
        msg = msg or self.end_message
        return f"{self._clean_message(msg)} {self._format_duration(self.elapsed)}"

    @staticmethod
    @typechecked
    def _format_duration(duration: float) -> str:
        """
        Summary:
            Take the `duration` as a float, and convert it to a string value identifying the number of minutes, seconds, etc.

        Params:
            duration (float):
                The duration to convert.

        Returns:
            str:
                The converted duration.

        ???+ Info "Details"
            Credit goes to: https://stackoverflow.com/questions/62198128/python-elapsed-time-as-days-hours-minutes-seconds#answer-62198639.
        """

        mapping = [
            ("secs", 60),
            ("mins", 60),
            ("hrs", 24),
        ]

        duration = int(duration)
        result = []

        for symbol, max_amount in mapping:
            amount = duration % max_amount
            result.append(f"{amount}{symbol}")
            duration //= max_amount
            if duration == 0:
                break

        return " ".join(reversed(result))

    @typechecked
    def _clean_message(self, message: str) -> str:
        """
        Summary:
            Clean a message.

        Params:
            message (str):
                The message to be cleaned.

        Returns:
            str:
                The cleaned message.

        ???+ Info "Details"
            Will perform the following steps:
                1. If `message` ends in whitespace (` `), it will strip the whitespace from the end.
                1. If `message` does not end with a colon (`:`), it will add the colon on the end.

        ???+ Example "Examples"
            _description_.
            ```python linenums="1"
            >>> from tictoc import TicToc
            >>> TicToc._clean_message("Total time:    ")
            Total time:
            >>> TicToc._clean_message("Total time")
            Total time:
            >>> TicToc._clean_message("Total time     ")
            Total time:
            ```
        """
        if message.endswith(" "):
            message = message.rstrip()
        if not message.endswith(":"):
            message = f"{message}:"
        return message
