'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

from pprint import pprint
from unicodedata import category
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Select all the actors with the first name of your choice
# actor_table = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

# query = sqlalchemy.select(actor_table).where(actor_table.columns.first_name == 'Matthew')
# result_proxy = connection.execute(query)

# for actor in result_proxy:
#     print(actor)


# Select all the actors and the films they have been in

# actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
# film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
# film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

# join_statement = actor.join(film_actor, film_actor.columns.actor_id == \
#     actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)

# query = sqlalchemy.select([film.columns.film_id, film.columns.title, actor.columns.first_name, \
#     actor.columns.last_name]).select_from(join_statement)

# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)


# Select all the actors that have appeared in a category of a comedy of your choice
# film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
# film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
# actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

# join_statement = film.join(film_actor, film_actor.columns.film_id == film.columns\
#     .film_id).join(actor, actor.columns.actor_id == film_actor.columns.actor_id)

# query = sqlalchemy.select([film.columns.title, actor.columns.first_name, actor.\
#     columns.last_name]).select_from(join_statement).where(film.columns.film_id == 404)

# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# Select all the comedic films and sort them by rental rate

# film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
# film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

# join_statement = film.join(film_category, film_category.columns.film_id == film.columns\
#     .film_id)

# query = sqlalchemy.select([film.columns.title, film.columns.rental_rate]).select_from(join_statement).\
#     where(film_category.columns.category_id == 5).order_by(sqlalchemy.desc(film.columns.rental_rate))

# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# Using one of the statements above, add a GROUP BY statement of your choice

actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == \
    actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)

query = sqlalchemy.select([film.columns.film_id, film.columns.title, actor.columns.first_name, \
    actor.columns.last_name]).select_from(join_statement)

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

grouped_result_set = result_set.groupby('title')
pprint(grouped_result_set)