import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

new_table = sqlalchemy.Table('new_table', metadata, autoload=True, autoload_with=engine)

# Adding multiple entries into a database
query = sqlalchemy.insert(new_table)
new_records = [{'id':'2', 'name':'Jane Doe', 'salary':'50000.00'},
                {'id':'3', 'name':'Johnny Appleseed', 'salary':'45000.00'}]

result_proxy = connection.execute(query, new_records)




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

