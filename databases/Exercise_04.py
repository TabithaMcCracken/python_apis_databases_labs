'''
Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!
'''
# We Need to:
# Create functions for each task: create tables, inser data, update data, select data, delete data, use a join
# Create a function to ask user which task to copmlete
# Call the which task function
# While loop to ask user if they want to complete another task, calls which task functino again or ends the session


from pprint import pprint
from tkinter import SW
import sqlalchemy
from secret import password

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{password}@localhost/Python201Exercise4')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Create 3 tables
# product_table = sqlalchemy.Table('product', metadata, \
#     sqlalchemy.Column('product_id', sqlalchemy.Integer()), \
#     sqlalchemy.Column('product_name', sqlalchemy.String(20), nullable=False), \
#     sqlalchemy.Column('product_desc', sqlalchemy.String(200), nullable=False), \
#     sqlalchemy.Column('product_price', sqlalchemy.Float(), default=100.00)    
#     )

# location_table = sqlalchemy.Table('location', metadata, \
#     sqlalchemy.Column('location_id', sqlalchemy.Integer()), \
#     sqlalchemy.Column('location_name', sqlalchemy.String(20), nullable=False), \
#     sqlalchemy.Column('tax_rate', sqlalchemy.Float(), default=10.00)
#     )

# customer_table = sqlalchemy.Table('customer', metadata, \
#     sqlalchemy.Column('customer_id', sqlalchemy.Integer()), \
#     sqlalchemy.Column('first_name', sqlalchemy.String(200), nullable=False), \
#     sqlalchemy.Column('last_name', sqlalchemy.String(200), nullable=False), \
#     sqlalchemy.Column('email', sqlalchemy.String(100), nullable=False), \
#     sqlalchemy.Column('location_id', sqlalchemy.Integer())
#     #sqlalchemy.ForeignKeyConstraint(['location_id'],['location.location_id'])- Doesn't work
#     )
# metadata.create_all(engine)

# Insert Data in each table 
# product = sqlalchemy.Table('product', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.insert(product)

# new_products = [ {'product_id':1, 'product_name':'Sleigh Sign', 'product_desc':"5x7 \
#                     Sleigh sign: It's Lovely Weather for a slegih ride together", 'product_price':20.00},
#                 {'product_id':2, 'product_name':'Gold Tree', 'product_desc':"9inch \
#                     Christmas tree: O Come Let Us Adore Him", 'product_price':20.00},
#                 {'product_id':3, 'product_name':'Small Spoons Game', 'product_desc': \
#                     "Six player spoons and LRC game", 'product_price':40.00}
#                 ]
# result_proxy = connection.execute(query, new_products)

# location = sqlalchemy.Table('location', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.insert(location)
# locations = [ {'location_id':1, 'location_name':'Home', 'tax_rate':6.25},
#             {'location_id':2, 'location_name':'Aurora', 'tax_rate':8.00},
#             {'location_id':3, 'location_name':'South Dakota', 'tax_rate':0.00}
#             ]
# result_proxy = connection.execute(query, locations)


# customer = sqlalchemy.Table('customer', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.insert(customer)
# customers = [ {'customer_id':1, 'first_name':'John', 'last_name':'Doe', 'email':'asdlfkja@gmail.com', 'location_id':1},
#             {'customer_id':2, 'first_name':'Jane', 'last_name':'Doe', 'email':'askja@gmail.com', 'location_id':1},
#             {'customer_id':3, 'first_name':'Curious', 'last_name':'George', 'email':'george@gmail.com', 'location_id':3}
#             ]
# result_proxy = connection.execute(query, customers)


# Update data in each table
# products = sqlalchemy.Table('product', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.update(products).values(product_price=25).where(products.columns.product_price == 20)
# result = connection.execute(query)

# locations = sqlalchemy.Table('location', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.update(locations).values(tax_rate=8.0).where(locations.columns.location_id == 1)
# result = connection.execute(query)

# customers = sqlalchemy.Table('customer', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.update(customers).values(last_name='Donut').where(customers.columns.last_name == 'Doe')
# result = connection.execute(query)


# Select data from each table
# product = sqlalchemy.Table('product', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.select([product]).where(product.columns.product_price == 25.00)
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# location = sqlalchemy.Table('location', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.select([location]).where(location.columns.location_id == 1)
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# customer = sqlalchemy.Table('customer', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.select([customer]).where(customer.columns.last_name == 'Donut')
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)


# Delete data from each table
# product_table = sqlalchemy.Table('product', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.delete(product_table).where(product_table.columns.product_price > 25.00)
# results = connection.execute(query)

location_table = sqlalchemy.Table('location', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.delete(location_table).where(location_table.columns.location_id == 3)
# results = connection.execute(query)

customer_table = sqlalchemy.Table('customer', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.delete(customer_table).where(customer_table.columns.first_name == 'Curious')
# results = connection.execute(query)


# Use at least one join in a select query
join_statement = customer_table.join(location_table, location_table.columns.location_id \
    == customer_table.columns.location_id)
query = sqlalchemy.select([location_table.columns.location_name, customer_table.columns.first_name, \
    customer_table.columns.last_name]).select_from(join_statement)

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)


# Other ideas for usage
# # Function asking which task to complete
# def which_task():
#     task = int(input(
#         "Please select from the following options (enter the number of the action "
#         "you'd like to take):\n"
#         "1) Create a new table\n"
#         "2) Insert new data into a table\n"
#         "3) Update data in a table\n"
#         "4) Select data in a table\n"
#         "5) Delete data from a table\n"
#         "6) Get sales summary by location\n"
     
#     ))
#     print(f"You have selected option: {task}")

#     if task == 1:
#         create_table()
#     elif task == 2:
#         insert_new_data()
#     elif task == 3:
#         update_data()
#     elif task == 4:
#         select_data()
#     elif task == 5:
#         delete_data()
#     elif task ==6:
#         sales_summary()

# which_task()

# # Ask to complete another task
# end_task_flag = False
# while end_task_flag == False:
#     another_task = input("Would you like to complete another option? Yes or No\n")
#     if another_task == "Yes":
#         which_task()
#         end_task_flag = False
#     elif another_task == "No":
#         end_task_flag = True
#     else:
#         print("Invalid response")
#         end_task_flag = False