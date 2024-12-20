import pandas as pd
from db_operations import create_table, load_data
from dotenv import load_dotenv
import os

# Working with hidden .env file with important information and configurations
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}

DATA_FILE = os.path.join(os.getcwd(), "data", "data.csv")

def extract(file_path):
    """
    Reads data from a CSV file using pandas.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: The extracted data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def transform(data):
    """
    Transforms the data by formatting columns and adding new information.

    Operations performed:
    - Converts the 'signup_date' column to the 'YYYY-MM-DD' format.
    - Extracts the email domain and adds it as a new column 'domain'.

    Parameters:
    - data (pd.DataFrame): The raw data to be transformed.

    Returns:
    - pd.DataFrame: The transformed data.
    """
    data['signup_date'] = pd.to_datetime(data['signup_date']).dt.strftime('%Y-%m-%d')
    data['domain'] = data['email'].apply(lambda x: x.split('@')[1])
    return data

if __name__ == "__main__":
    print("Staring ETL process...")

    # Extract
    raw_data = extract(DATA_FILE)
    print("Data has been successfully read.")

    # Transform
    transformed_data = transform(raw_data)
    print("Data has been successfully transformed.")

    # Load
    create_table(DB_CONFIG)
    load_data(transformed_data, DB_CONFIG)
    print("Data has been successfully loaded into the database.")
