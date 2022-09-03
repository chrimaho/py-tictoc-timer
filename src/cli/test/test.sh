python -m pipenv run python -m pytest --verbose --cov=py_tictoc --cov-report=term --cov-report=html:cov-report/html --cov-report=xml:cov-report/xml/cov-report.xml

pipenv run pytest --verbose --cov=py_tictoc --cov-report=term --cov-report=html:cov-report/html --cov-report=xml:cov-report/xml/cov-report.xml

pipenv run mypy py_tictoc --ignore-missing-imports --pretty --install-types --non-interactive
