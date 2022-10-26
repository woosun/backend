FROM python:3.8
ADD ./* /
RUN pip install -y Flask Flask-Cors gunicorn
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app