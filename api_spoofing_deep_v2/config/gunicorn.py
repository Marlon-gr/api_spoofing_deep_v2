import os

bind = "0.0.0.0:9000"
workers = os.environ.get('GUNICORN_WORKERS', 2)
timeout = os.environ.get('GUNICORN_TIMEOUT', 60)
keepalive = os.environ.get('GUNICORN_KEEPALIVE', 60)
capture_output = True
worker_class = os.environ.get('GUNICORN_WORKER_CLASS', "gthread")
threads = os.environ.get('GUNICORN_THREADS', 4)
worker_connections = os.environ.get('GUNICORN_WORKER_CONNECTIONS', 1000)