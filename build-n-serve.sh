#!/bin/bash
docker build . \
  -t workout-manager
docker run \
  -it \
  -p 8080:80 \
  -v $(pwd)/db.sqlite3:/app/db.sqlite3 \
  workout-manager
