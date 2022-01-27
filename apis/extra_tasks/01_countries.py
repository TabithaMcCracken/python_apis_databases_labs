'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
# Get the data
# Ask the user which country to view
# Find data for only that country

import requests
import json

base_url = "https://restcountries.com/v3/all"

# Get user input and data for those countries
home_country = input("Please input your home country: ")
current_country = input("Please input the country you currently live in: ")

home_url = f"https://restcountries.com/v3/name/{home_country}"
r = requests.get(home_url)
home_data = r.json()

current_url = f"https://restcountries.com/v3/name/{current_country}"
s = requests.get(current_url)
current_data = s.json()


# Which country has the larger population?

# Get population of each country
home_pop = home_data[0]["population"]
current_pop = current_data[0]["population"]

print(f"The population of {home_country} is: {home_pop}")
print(f"The population of {current_country} is: {current_pop}")

if home_pop > current_pop:
    print(f"{home_country} has a bigger population.")
elif current_pop > home_pop:
    print(f"{current_country} has a bigger population.")
else:
    print(f"Wow, they have the same population!")

# How much does the are of the two countries differ?
home_area = home_data[0]["area"]
current_area = current_data[0]["area"]

if home_area > current_area:
    area_dif = home_area - current_area
elif current_area > home_area:
    area_dif = current_area - home_area

print(f"The difference in the area of the two countries is: {area_dif}")


# Print the native name of both countries, as well as their capitals
native_name = home_data[0]["name"]["nativeName"]
capital = home_data[0]["capital"]
print(f"The native name for {home_country} is: {native_name}")
print(f"The capital of {home_country} is: {capital}")


native_name2 = current_data[0]["name"]["nativeName"]
capital2 = current_data[0]["capital"]
print(f"The native name for {current_country} is: {native_name2}")
print(f"The capital of {current_country} is: {capital2}")






