FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

COPY backend ./backend

COPY models ./models

WORKDIR /app/backend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]