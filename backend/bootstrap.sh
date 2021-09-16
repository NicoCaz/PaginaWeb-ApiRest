export FLASK_APP=./api-usuario/main.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0