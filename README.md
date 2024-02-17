
### Usage

1. Start the Docker containers:

   ```bash
   docker compose up
   ```

   - To run the containers in detached mode, use `docker-compose up -d`.

2. Build the Docker images (if needed):

   ```bash
   docker compose build
   ```

3. To run just the Django application:

   ```bash
   docker compose run django
   ```

4. To access the Django container's shell:

   ```bash
   docker compose exec django bash
   ```