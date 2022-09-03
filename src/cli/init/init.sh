if (-not (Test-Path .venv)) {mkdir .venv}
python -m pipenv install typeguard --ignore-pipfile --skip-lock --no-site-packages
python -m pipenv install --requirements requirements.txt --ignore-pipfile --skip-lock --no-site-packages
python -m pipenv install --requirements requirements-dev.txt --dev --ignore-pipfile --skip-lock --no-site-packages
python -m pipenv run python -m pip install --upgrade pip
python -m pipenv run python -m poetry install
