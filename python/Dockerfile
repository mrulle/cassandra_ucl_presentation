FROM python:3.9.18-bullseye
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY ./test.py /app/test.py
RUN ["pip", "install", "-r", "/app/requirements.txt"]
ENTRYPOINT [ "python", "-u", "test.py" ]

