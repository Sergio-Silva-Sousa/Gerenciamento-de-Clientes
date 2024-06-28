from peewee import MySQLDatabase
from dotenv import load_dotenv
import os
load_dotenv()
DATABASE=os.getenv("DATABASE","")
USER=os.getenv("USER","")
PASSWORD=os.getenv("PASSWORD","")
HOST=os.getenv("HOST","")
PORT=os.getenv("USER","0")
# Use Postgres (and register hstore extension).
db = MySQLDatabase(DATABASE, 
                         user=USER,
                         password=PASSWORD,
                         host=HOST, 
                         port=3306)
