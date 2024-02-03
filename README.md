# llm-flask-app
Simple flask application with tiny llm onboard

gunicorn --chdir app -c app/gunicorn_config.py 'server:app' --timeout 600
