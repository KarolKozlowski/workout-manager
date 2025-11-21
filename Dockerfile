FROM python:3-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY /wmsite /app/wmsite
COPY /wmapp /app/wmapp
COPY ./manage.py /app/manage.py
COPY --chmod=755 ./entrypoint.sh /app/entrypoint.sh
COPY ./gunicorn_conf.py /app/gunicorn_conf.py

CMD ["/app/entrypoint.sh"]