python -m pipenv run python -m pytest --verbose --cov=tictoc_timer --cov-report=term --cov-report=html:cov-report/html --cov-report=xml:cov-report/xml/cov-report.xml

pipenv run pytest --verbose --cov=tictoc_timer --cov-report=term --cov-report=html:cov-report/html --cov-report=xml:cov-report/xml/cov-report.xml

pipenv run mypy tictoc_timer --ignore-missing-imports --pretty --install-types --non-interactive
