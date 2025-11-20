FROM python:3-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY /workoutmanager /app/workoutmanager
COPY ./gunicorn_conf.py /app/gunicorn_conf.py

CMD ["gunicorn", "--conf", "/app/gunicorn_conf.py", "--bind", "0.0.0.0:80", "workoutmanager.wsgi:application"]