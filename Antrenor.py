class Antrenor:
    def __init__(self, nume, pokemoni):
        self.nume = nume
        self.pokemoni = pokemoni

    def alege_pokemon(self):
        print(self.nume, "--> Pick your pokemon:")
        for i in range(len(self.pokemoni)):
            print(f'{i+1}. {self.pokemoni[i].nume}')
        choice = input("Your choice: ")
        return self.pokemoni[int(choice) - 1]

    def are_pokemoni_vii(self):
        return any(pokemon.este_viu() for pokemon in self.pokemoni)

    def __repr__(self):
        return f'Trainer: {self.nume} --> Pokemons: {self.pokemoni}'
