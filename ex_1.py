class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def pokemon_info(self):
        print(f"Name: {self.name} Level: {self.level}")

class Collector:
    def __init__(self):
        self.pokemons = []

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def collection_info(self):
        for pokemon in self.pokemons:
            pokemon.pokemon_info()


