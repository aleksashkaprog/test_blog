FROM python:3.9.0-slim
RUN mkdir /app

COPY requirements.txt /app/


RUN python -m pip install -r /app/requirements.txt

COPY manage.py /app/

WORKDIR /app

ENTRYPOINT ["python", "manage.py"]