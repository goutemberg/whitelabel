#!/bin/sh

echo "Iniciando o servidor Gunicorn..."
gunicorn pedilaso.asgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --worker-class uvicorn.workers.UvicornWorker