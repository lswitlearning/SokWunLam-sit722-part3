import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password123*@sit22project.postgres.database.azure.com:5432/inventory')
