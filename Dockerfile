FROM python:3-alpine

# Set environment variables
# Prevents Python from writing pyc files to disc
# and forces stdout and stderr to be unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	DJANGO_SETTINGS_ENV=prod

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
# Install pip dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy project sources
COPY wmsite /app/wmsite
COPY wmapi /app/wmapi
COPY wmapp /app/wmapp
COPY manage.py /app/manage.py
COPY entrypoint.sh /app/entrypoint.sh
COPY gunicorn_conf.py /app/gunicorn_conf.py

RUN chmod +x /app/entrypoint.sh

EXPOSE 80

CMD ["/app/entrypoint.sh"]