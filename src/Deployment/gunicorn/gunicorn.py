"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count


def max_workers():
    return cpu_count() * 2 + 1

max_requests = 40000
worker_class = 'gevent'
workers = max_workers()
