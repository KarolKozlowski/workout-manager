#!/bin/bash
docker build -t workout-manager .
docker run \
  -it \
  -p 8000:80 \
  -e DJANGO_SETTINGS_ENV=dev \
  -v $(pwd)/db:/app/db:rw \
  workout-manager
