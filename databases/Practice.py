import sqlalchemy
from pprint import pprint
from actor2 import Actor

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([actor])
result_proxy = connection.execute(query)

actor_list = []
for result in result_proxy:
    new_actor = Actor(result['actor_id'], result['first_name'], result['last_name'], result['last_update'])
    actor_list.append(new_actor)

for actor in actor_list:
    print(actor)


# Print all results first and last name
# for result in result_proxy:
#     print(f"First Name: {result['first_name']}")
#     print(f"Last Name: {result['last_name']}")

# Print in an f string
# result = result_proxy.fetchone()
# print(f"First Name: {result['first_name']}")
# print(f"Last Name: {result['last_name']}")

# Print first record
# result = result_proxy.fetchone()
# print(result.keys())

# Iterate over list
# for actor in actor_list:
#     print(actor)

# Print first record
# result = result_proxy.fetchone()
# print(result)

# Print all in the result set
# for result in result_proxy:
#    print(result)

# Delete 
# new_table = sqlalchemy.Table('new_table', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.delete(new_table).where(new_table.columns.salary < 100000.00)
# results = connection.execute(query)

# Update an entry
# new_table = sqlalchemy.Table('new_table', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.update(new_table).values(salary=100000.00).where(new_table.columns.id == 1)
# result_proxy = connection.execute(query)

# Adding multiple entries into a database sakila
# query = sqlalchemy.insert(new_table)
# new_records = [{'id':'2', 'name':'Jane Doe', 'salary':'50000.00'},
#                 {'id':'3', 'name':'Johnny Appleseed', 'salary':'45000.00'}]
# result_proxy = connection.execute(query, new_records)

# Join
# actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
# film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
# film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, \
#     autoload_with=engine)

# join_actor_film_actor = actor.join(film_actor, film_actor.columns.actor_id == \
#     actor.columns.actor_id)
# join_statement = join_actor_film_actor.join(film, film.columns.film_id == \
#     film_actor.columns.film_id)
# query = sqlalchemy.select([film.columns.title, actor.columns.first_name]).select_from(join_statement)

# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

