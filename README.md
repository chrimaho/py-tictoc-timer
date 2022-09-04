# tictoc-timer
Time the execution of Python code using syntax similar to MATLAB's tic and toc functions.

[![codecov](https://codecov.io/gh/chrimaho/tictoc-timer/branch/main/graph/badge.svg)](https://codecov.io/gh/chrimaho/tictoc-timer)
[![Unit Testing](https://github.com/chrimaho/tictoc-timer/actions/workflows/unit-tests.yml/badge.svg?branch=main)](https://github.com/chrimaho/tictoc-timer/actions/workflows/unit-tests.yml)
[![Publish Package](https://github.com/chrimaho/tictoc-timer/actions/workflows/pypi-publish.yml/badge.svg?branch=main)](https://github.com/chrimaho/tictoc-timer/actions/workflows/pypi-publish.yml)

- [tictoc-timer](#tictoc-timer)
  - [Installation](#installation)
    - [Using `pip`:](#using-pip)
    - [Using `pipenv`:](#using-pipenv)
    - [Using `poetry`:](#using-poetry)
    - [Using `conda`](#using-conda)
  - [Usage](#usage)
  - [Contribution](#contribution)
  - [Build & Test](#build--test)
    - [Run Black](#run-black)
    - [Run PyTests:](#run-pytests)
    - [Run MyPy Tests:](#run-mypy-tests)

## Installation

### Using [`pip`](https://pypi.org/project/pip):
```sh
pip install tictoc-timer
```

### Using [`pipenv`](https://github.com/pypa/pipenv):
```sh
pipenv install tictoc-timer
```

### Using [`poetry`](https://python-poetry.org):
1. In your `pyproject.toml` file, add:
    ```toml
    [tool.poetry.dependencies]
    tictoc-timer
    ```
2. Then in the terminal, run:
    ```sh
    poetry install
    ```

### Using [`conda`](https://docs.conda.io)
```sh
conda install tictoc-timer
```

## Usage

Basic usage:
```python linenums="1"
>>> from tictoc import TicToc
>>> from time import sleep
>>> tt = TicToc()
>>> tt.tic()
>>> sleep(1.1)
>>> tt.toc()
Elapsed time: 1secs
```

Within context manager:
```python linenums="1"
>>> from tictoc import TicToc
>>> from time import sleep
>>> with TicToc():
...     sleep(1.1)
Elapsed time: 1secs
```

Within context manager using custom messages:
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

## Contribution
All contributions are welcome!

## Build & Test

### Run [Black](https://black.readthedocs.io/)
```sh
python -m pipenv run python -m black --safe tictoc_timer tests
```

### Run [PyTests](https://docs.pytest.org):
```sh
python -m pipenv run python -m pytest --verbose --cov=tictoc_timer --cov-report=term --cov-report=html:cov-report/html --cov-report=xml:cov-report/xml/cov-report.xml
```

### Run [MyPy](http://www.mypy-lang.org) Tests:
```sh
pipenv run mypy tictoc_timer --ignore-missing-imports --pretty --install-types --non-interactive
```
