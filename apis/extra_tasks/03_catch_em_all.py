'''
Using the PokéAPI https://pokeapi.co/docs/v2#pokemon-section
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''
import requests
import json

pokemon_list = []

base_url = "https://pokeapi.co/api/v2/pokemon/"
r = requests.get(base_url)
data = r.json()

print(data)

for pokemon in data:
       access = pokemon[0]
       pokemon_list.append(access)

print(pokemon_list)