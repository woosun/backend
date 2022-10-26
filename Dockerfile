FROM python:3.8
ADD ./* /
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app