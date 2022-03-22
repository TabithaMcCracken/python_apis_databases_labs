'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

# We Need:
# Function to get the users and tasks from the url
# Create tables
# Check to see if data already exists in the tables
# Put data in tables

from pprint import pprint
import sqlalchemy
from secret import password

