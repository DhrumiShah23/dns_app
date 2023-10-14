
FROM alpine:3.15

WORKDIR /app

RUN apk add --update python3 py3-pip && pip3 install flask

COPY ./AS /app

EXPOSE 53533/udp

CMD ["python3", "asserver.py"]
