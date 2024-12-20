import psycopg2

def create_table(config):
    """
    Creates the 'users' table in PostgreSQL if it doesn't exist.

    Parameters:
    - config (dict): A dictionary containing database connection parameters:
        - host: Database host.
        - database: Database name.
        - user: Database user.
        - password: User's password.
        - port: Database port.

    Returns:
    None
    """
    query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        signup_date DATE NOT NULL,
        domain TEXT NOT NULL
    );
    """
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
        print("Table 'users' was successfully created or already exists.")
    except Exception as e:
        print(f"problem with creating: {e}")

def load_data(data, config):
    """
    Loads data from a DataFrame into the 'users' table in PostgreSQL.

    Parameters:
    - data (pd.DataFrame): The pandas DataFrame containing the data to be loaded.
        Expected columns: ['user_id', 'name', 'email', 'signup_date', 'domain'].
    - config (dict): A dictionary containing database connection parameters:
        - host: Database host.
        - database: Database name.
        - user: Database user.
        - password: User's password.
        - port: Database port.

    Returns:
    None
    """
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                for _, row in data.iterrows():
                    cursor.execute(
                        """
                        INSERT INTO users (user_id, name, email, signup_date, domain)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (email) DO NOTHING;
                        """,
                        (row['user_id'], row['name'], row['email'], row['signup_date'], row['domain'])
                    )
                conn.commit()
        print("Data successfully loaded into 'users' table.")
    except Exception as e:
        print(f"Failed to load data into 'users' table. Problem: {e}")
