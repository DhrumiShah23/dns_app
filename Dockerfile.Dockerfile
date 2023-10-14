
FROM python:3.8-slim

WORKDIR /app

RUN pip install flask

COPY ./FS /app

EXPOSE 9090

CMD ["python", "fsserver.py"]
