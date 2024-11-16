#!/bin/bash

# Extract static files if tar exists
if [ -f /app/static.tar ]; then
    tar xf /app/static.tar -C /app/staticfiles/
fi

# Run gunicorn
exec gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --worker-class gthread \
    --threads 2 \
    --timeout 60 \
    --keep-alive 5 \
    --log-level warning \
    --access-logfile - \
    --error-logfile - \
    rafatech.wsgi:application
