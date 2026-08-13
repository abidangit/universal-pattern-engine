# Run with Docker Compose (example)

1. Copy .env.example to .env and edit DATABASE_URL and REDIS_URL
2. Build and run:

   docker compose up --build -d

3. View logs:

   docker compose logs -f api

4. Run migrations inside the API container:

   docker compose exec api alembic upgrade head

5. Stop:

   docker compose down
