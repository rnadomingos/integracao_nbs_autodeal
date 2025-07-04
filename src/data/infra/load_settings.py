import os
from pathlib import Path
from dotenv import load_dotenv

def load_settings() -> dict:
    
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
      "db_host": os.getenv("MYSQL_HOST"),
      "db_user": os.getenv("MYSQL_USER"),
      "db_pass": os.getenv("MYSQL_PASSWORD"),
      "db_name": os.getenv("MYSQL_DB"),
      "db_port": os.getenv("MYSQL_PORT"),
    }

    return settings