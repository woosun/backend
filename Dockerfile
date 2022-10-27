FROM python:3.9
ADD ./* /
RUN pip install -r /requirements.txt
EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8080 wsgi:app