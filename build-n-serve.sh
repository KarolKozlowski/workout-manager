#!/bin/bash
docker build -t workout-manager .

# Comma-separated IPv4 addresses for Django ALLOWED_HOSTS
DISCOVERED_INTERFACE_IPS="$(
  {
    echo "localhost"
    echo "127.0.0.1"
    hostname -I | tr ' ' '\n' | sed '/^$/d'
  } | sort -u | paste -sd, -
)"

docker run \
  -it \
  -p 8000:80 \
  -e DJANGO_SETTINGS_ENV=dev \
  -e "DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS:-$DISCOVERED_INTERFACE_IPS}" \
  -v "$(pwd)/db:/app/db:rw" \
  workout-manager
