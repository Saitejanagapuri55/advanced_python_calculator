import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Example of accessing environment variables
API_KEY = os.getenv("API_KEY")  # Replace with your actual variable names
DB_URL = os.getenv("DB_URL")    # Replace with your actual variable names
