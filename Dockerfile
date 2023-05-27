FROM python:3.10

WORKDIR /app

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY . .

RUN mkdir /fastapi
CMD uvicorn src.main:app --host 0.0.0.0 --port 8000"