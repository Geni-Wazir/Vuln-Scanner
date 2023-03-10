#!/bin/sh

# set -euo pipefail

# WORKERS=${WORKERS:-1}
# WORKER_CLASS=${WORKER_CLASS:-gevent}
# ACCESS_LOG=${ACCESS_LOG:--}
# ERROR_LOG=${ERROR_LOG:--}
# WORKER_TEMP_DIR=${WORKER_TEMP_DIR:-/dev/shm}
# SECRET_KEY=${SECRET_KEY:-}

# Check that a .ctfd_secret_key file or SECRET_KEY envvar is set
# if [ ! -f .ctfd_secret_key ] && [ -z "$SECRET_KEY" ]; then
#     if [ $WORKERS -gt 1 ]; then
#         echo "[ ERROR ] You are configured to use more than 1 worker."
#         echo "[ ERROR ] To do this, you must define the SECRET_KEY environment variable or create a .ctfd_secret_key file."
#         echo "[ ERROR ] Exiting..."
#         exit 1
#     fi
# fi

# Ensures that the database is available
# python ping.py

# Initialize database
# python manage.py db upgrade

# Start CTFd
echo "Starting Scanner"
exec gunicorn -w 1 -b 0.0.0.0:5000 wsgi:app