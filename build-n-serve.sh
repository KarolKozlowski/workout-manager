#!/bin/bash
docker build -t workout-manager .
docker run \
  -it \
  -p 8080:80 \
  -e DJANGO_DEBUG=True \
  -v $(pwd)/db/db.sqlite3:/app/db/db.sqlite3 \
  workout-manager
