# Simple ETL Pipeline with Docker

## Description
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL. The pipeline extracts data from a CSV file, applies necessary transformations, and loads the data into a PostgreSQL database. The entire application is containerized using Docker and Docker Compose for easy setup and deployment.

## Project Structure
```
DATA_TASK/
├── data/                  # Data directory containing the CSV file
│   └── data.csv           # Auto-generated dataset
├── etl/                   # Python scripts for ETL
│   ├── db_operations.py   # Handles database table creation and data insertion
│   ├── etl_pipeline.py    # Main script to run the ETL process
│   └── generate_data.py   # Generates a dataset using Faker
├── sql/                   # SQL scripts for analysis
│   └── queries.sql        # Predefined SQL queries for analysis
├── .env                   # Environment variables (not included in repo)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Dockerfile for building the app image
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # Project documentation
```

---

## Features
- **ETL Pipeline**:
  - **Extract**: Reads data from a CSV file.
  - **Transform**: Formats and validates data, adds a domain column extracted from email addresses.
  - **Load**: Inserts transformed data into a PostgreSQL database.
- **SQL Queries**:
  - Analyze user signup trends.
  - Retrieve unique email domains.
  - Identify users who signed up in the last 7 days.
  - Find the most popular email domain.
  - Delete records with unwanted email domains.
- Fully containerized with **Docker Compose**.

---

## Requirements

- **Docker Desktop** (latest version)
- **Git** (for cloning the repository)
- **Python 3.10+** (optional, for local script testing)
- **PostgreSQL** for managing the database

---

## Setup and Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/DATA_TASK.git
    cd DATA_TASK
    ```

2. **Set up environment variables**:
   - Create a `.env` file in the root directory:
      ```env
      DB_HOST=postgres_db
      DB_NAME=fast_api_study
      DB_USER=postgres
      DB_PASSWORD=2111
      DB_PORT=5432
      ```

3. **Build and run the Docker containers**:
    ```bash
    docker-compose up --build
    ```

4. **Verify the ETL process**:
    - Check the logs of the `etl_app` container to ensure the ETL process ran successfully:
      ```bash
      docker logs etl_app
      ```

---

## API Endpoints

### SQL Queries

1. **Count the number of users who signed up on each date**:
   ```sql
   SELECT signup_date, COUNT(*) AS user_count
   FROM users
   GROUP BY signup_date
   ORDER BY signup_date;
   ```
   
2. **List all unique email domains**:
```sql
SELECT DISTINCT domain FROM users;
Users signed up in the last 7 days:
```

3. **Retrieve all users who signed up within the last 7 days**:
```sql
SELECT * FROM users WHERE signup_date >= CURRENT_DATE - INTERVAL '7 days';
Most popular email domain:
```

4. **The most popular domain**:
```sql
SELECT domain, COUNT(*) AS domain_count
FROM users
GROUP BY domain
ORDER BY domain_count DESC
LIMIT 1;
```
   **Users with the most popular domain**:
```sql
SELECT *
FROM users
WHERE domain = (
    SELECT domain
    FROM users
    GROUP BY domain
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
``` 

5. **Delete records where the email domain is not from the allowed list**:
```sql
DELETE FROM users
WHERE domain NOT IN ('gmail.com', 'yahoo.com', 'example.com');
```
## Testing

1. Configure the .env file correctly.
2. Download the reuirements file using:
   ```bash
   pip install -r requirements.txt
   ```
3. Use the 'docker-compose up --build' to start the containers:
   ```bash
   docker-compose up --build
   ```
4. Verify the ETL process by checking the data in the `users` table after the pipeline runs.
5. Run all SQL queries to validate database operations and transformations.
6. Use `docker-compose down` to stop the containers after testing:
   ```bash
   docker-compose down
   ```


###Known Issues

1. Ensure the .env file is correctly configured before running the containers.
2.  the data.csv file is missing, rerun the ETL pipeline to regenerate it.


