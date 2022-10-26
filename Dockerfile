FROM python:3.8
ADD ./* /
RUN pip install Flask Flask-Cors gunicorn pymysql
CMD gunicorn --bind 0.0.0.0:8080 wsgi:app