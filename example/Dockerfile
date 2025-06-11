FROM python:3.13-alpine

RUN pip install flask psycopg[binary]

WORKDIR app

COPY app.py /app
COPY index.html /app

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3000"]
