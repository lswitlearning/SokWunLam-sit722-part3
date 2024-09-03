#inventory_management
FROM python:3.12-slim
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /usr/src/app/app

ENV DATABASE_URL="postgresql://user:password123*@sit22project.postgres.database.azure.com:5432/postgres"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

