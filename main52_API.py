# Connecting to API

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Data retrieved.")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

def show_pokemon_info(pokemon_info):
    if pokemon_info:
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"Id: {pokemon_info["id"]}")
        print(f"Height: {pokemon_info["height"]}")
        print(f"Weight: {pokemon_info["weight"]}")

pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)
show_pokemon_info(pokemon_info)

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)
show_pokemon_info(pokemon_info)
