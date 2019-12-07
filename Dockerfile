FROM python:3-alpine 

LABEL version="1.0"
LABEL maintainer="bruno_engineer@hotmail.com"
LABEL description="Flask App - User Manager Service"

WORKDIR /app
COPY . .
RUN pip install flask

VOLUME [ "/tmp", "/tmp" ]

ENV FLASK_APP=/app/app.py

EXPOSE 8080

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]
