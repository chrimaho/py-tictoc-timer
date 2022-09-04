<div align="center">

# `py-tictoc-timer`

[![PyPI version](https://img.shields.io/pypi/v/py-tictoc-timer?label=version)](https://img.shields.io/pypi/v/py-tictoc-timer?label=version)
[![Python](https://img.shields.io/pypi/pyversions/py-tictoc-timer.svg?style=plastic&logo=python)](https://badge.fury.io/py/py-tictoc-timer)<br>
[![Released](https://img.shields.io/github/release-date/chrimaho/py-tictoc-timer)](https://img.shields.io/github/release-date/chrimaho/py-tictoc-timer)
[![Unit Testing](https://img.shields.io/github/workflow/status/chrimaho/py-tictoc-timer/Unit%20Testing/main?label=testing&logo=pytest)](https://github.com/chrimaho/py-tictoc-timer/actions/workflows/unit-tests.yml)
[![Publish Package](https://img.shields.io/github/workflow/status/chrimaho/py-tictoc-timer/Publish%20Package?label=build&logo=pypi)](https://github.com/chrimaho/py-tictoc-timer/actions/workflows/pypi-publish.yml)
[![codecov](https://codecov.io/gh/chrimaho/py-tictoc-timer/branch/main/graph/badge.svg)](https://codecov.io/gh/chrimaho/py-tictoc-timer)<br>
[![Vulnerabilities](https://img.shields.io/snyk/vulnerabilities/github/chrimaho/py-tictoc-timer)](https://img.shields.io/snyk/vulnerabilities/github/chrimaho/py-tictoc-timer)
[![License](https://img.shields.io/pypi/l/py-tictoc-timer)](https://img.shields.io/pypi/l/py-tictoc-timer)
<!-- [![Downloads](https://img.shields.io/pypi/dm/py-tictoc-timer)](https://github.com/chrimaho/py-tictoc-timer) -->
<!-- [![Stability](https://img.shields.io/pypi/status/py-tictoc-timer)](https://img.shields.io/pypi/status/py-tictoc-timer) -->

</div>

Time the execution of Python code using syntax similar to MATLAB's tic and toc functions.

<table>
<td>

**Contents**

- [`py-tictoc-timer`](#py-tictoc-timer)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contribution](#contribution)
  - [Tests](#tests)
  - [Credit](#credit)
  - [Maintainers](#maintainers)

</td>
</table>

## Installation

- Using [`pip`](https://pypi.org/project/pip):
  ```sh
  pip install py-tictoc-timer
  ```

- Using [`pipenv`](https://github.com/pypa/pipenv):
  ```sh
  pipenv install py-tictoc-timer
  ```

- Using [`poetry`](https://python-poetry.org):
  1. In your `pyproject.toml` file, add:
      ```toml
      [tool.poetry.dependencies]
      py-tictoc-timer = "*"
      ```
  2. Then in the terminal, run:
      ```sh
      poetry install
      ```

- Using [`conda`](https://docs.conda.io):
  ```sh
  conda install py-tictoc-timer
  ```

## Usage

- Basic usage:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> tt = TicToc()
  >>> tt.tic()
  >>> sleep(1.1)
  >>> tt.toc()
  Elapsed time: 1secs
  ```

- Within context manager:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> with TicToc():
  ...     sleep(1.1)
  Elapsed time: 1secs
  ```

- Within context manager using custom messages:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> with TicToc(begin_message="start", end_message="end"):
  ...     sleep(1.1)
  start
  end: 1secs
  ```

- Custom message:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> with TicToc("Total Time"):
  ...     sleep(1.1)
  Total time: 1secs
  ```

- With restart during `.tic()`:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> tt = TicToc()
  >>> tt.tic(restart=True)
  >>> sleep(1.1)
  >>> toc()
  Elapsed time: 1secs
  >>> toc()
  Elapsed time: 1secs
  ```

- With restart during `.toc()`:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> tt = TicToc()
  >>> tt.tic()
  >>> sleep(1.1)
  >>> tt.toc(restart=True)
  Elapsed time: 1secs
  >>> tt.toc()
  Elapsed time: 1secs
  ```

- With restart using `.rtoc()`:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> tt = TicToc()
  >>> tt.tic()
  >>> sleep(1.1)
  >>> tt.rtoc()
  Elapsed time: 1secs
  >>> tt.toc()
  Elapsed time: 1secs
  ```

- With time returned:
  ```python linenums="1"
  >>> from py_tictoc_timer.tictoc import TicToc
  >>> from time import sleep
  >>> tt = TicToc()
  >>> tt.tic()
  >>> sleep(1.1)
  >>> value = tt.toc_value()
  >>> print(round(value, 1))
  1.1
  ```

## Contribution
1. First, either [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) or [branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository#creating-a-branch) the [main repo](https://github.com/chrimaho/py-tictoc-timer/tree/main).
2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) your forked/branched repo.
3. Build your environment:
   1. With [`pipenv`](https://github.com/pypa/pipenv):
        ```sh
        if (-not (Test-Path .venv)) {mkdir .venv}
        python -m pipenv install --requirements requirements.txt --ignore-pipfile --skip-lock --no-site-packages
        python -m pipenv install --requirements requirements-dev.txt --dev --ignore-pipfile --skip-lock --no-site-packages
        python -m pipenv run pre-commit install
        ```
   2. With [`poetry`](https://python-poetry.org/) on Windows:
        ```sh
        (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
        python -m poetry run pre-commit install
        ```
   3. With [`poetry`](https://python-poetry.org/) on Linux:
        ```sh
	    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
        python -m poetry run pre-commit install
        ```
4. Start contributing.
5. Ensure you add additional [Unit Test](https://docs.python.org/3/library/unittest.html)s to the [test library](https://github.com/chrimaho/py-tictoc-timer/blob/main/tests/test_tictoc.py) for each new feature/functionality.
6. Ensure that all the [tests](#tests) are passing successfully.
7. When you're happy with the changes, raise a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to merge with the [main](https://github.com/chrimaho/py-tictoc-timer/tree/main) branch again.

## Tests

- Run [Black](https://black.readthedocs.io/):
  ```sh
  pipenv run python -m black --safe py_tictoc_timer tests
  ```

- Run [PyTests](https://docs.pytest.org):
  ```sh
  pipenv run python -m pytest --verbose --cov=py_tictoc_timer --cov-report=term --cov-report=html:cov-report/html --cov-report=xml:cov-report/xml/cov-report.xml
  ```

- Run [MyPy](http://www.mypy-lang.org) Tests:
  ```sh
  pipenv run mypy py_tictoc_timer --ignore-missing-imports --pretty --install-types --non-interactive
  ```

## Credit

This package was inspired by a few other packages:
- [`pytictoc`](https://pypi.org/project/pytictoc/)
- [`TicTocTimer`](https://pypi.org/project/tictoctimer/)
- [`ttictoc`](https://pypi.org/project/ttictoc/)
- [`easy-tictoc`](https://pypi.org/project/easy-tictoc/)
- [`easy-tic-toc`](https://pypi.org/project/easy-tic-toc/)
- [`tictoc-borisgorelik`](https://pypi.org/project/tictoc-borisgorelik/)

The differentiator is:
1. To restart the timer easier
2. The custom messages
3. The enhanced usage within a context manager

## Maintainers
<a href="https://github.com/chrimaho/py-tictoc-timer/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=chrimaho/py-tictoc-timer" width=40/>
</a>
