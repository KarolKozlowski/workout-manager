#!/bin/sh

set -x

is_true() {
  value="$1"
  # Convert to lowercase using tr
  value_lower=$(echo "$value" | tr '[:upper:]' '[:lower:]')

  case "$value_lower" in
    1|true|yes|y)
      return 0  # true
      ;;
    *)
      return 1  # false
      ;;
  esac
}

# perform database migrations
python3 manage.py migrate --run-syncdb

# load initial exercise data
python3 manage.py load_exercises

if is_true "$DEBUG"; then
  echo "Running in debug mode, static files will be served by Django development server."
  python3 manage.py runserver 0.0.0.0:80
else
  echo "Running in production mode, static files will be collected but NOT served by Gunicorn."
  # collect static files
  python3 manage.py collectstatic --noinput

  # start the Gunicorn server
  gunicorn --conf /app/gunicorn_conf.py --bind 0.0.0.0:80 wmsite.wsgi:application
fi
