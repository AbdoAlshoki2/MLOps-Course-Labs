FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install .

EXPOSE 5000

CMD ["litestar", "--app", "main:app", "run", "--host", "0.0.0.0", "--port", "5000"]