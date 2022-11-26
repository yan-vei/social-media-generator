FROM python:3.10.1-slim
ENV DB_CONTAINER_NAME db
COPY . /app
WORKDIR /app
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install -r requirements.txt
WORKDIR /app/src
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]