import csv
from faker import Faker
from datetime import datetime

faker = Faker()

NUM_RECORDS = 1000
SAVE_FILE  = "../data/data.csv"

def gen_fake_data(file_path, num_records):
    """
    Generates a fake dataset with the specified number of records and saves it to a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file where data will be saved.
    - num_records (int): Number of records to generate.

    Returns:
    None
    """
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'name', 'email', 'signup_date'])
        
        for user_id in range(1, num_records + 1):
            name = faker.name()
            email = faker.email()
            signup_date = faker.date_between(start_date='-2y', end_date='today')
            writer.writerow([user_id, name, email, signup_date])

    print(f"Fake dataset with {num_records} has been created on path: {file_path}")
    
if __name__ == "__main__":
    gen_fake_data(SAVE_FILE, NUM_RECORDS)