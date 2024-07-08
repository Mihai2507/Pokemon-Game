class Batalie:
    def lupta(self, antrenor1, antrenor2):
        print(f'Fight starts beetween {antrenor1} and {antrenor2}\n')
        pokemon1 = antrenor1.alege_pokemon()
        pokemon2 = antrenor2.alege_pokemon()
        while True:
            pokemon1.ataca(pokemon2)
            print(f'{pokemon1.nume} attacks {pokemon2.nume}, {pokemon2.nume} health: {pokemon2.viata}')

            if not pokemon2.este_viu():
                print(f'{pokemon2.nume} has been defeated!')
                for i in range(len(antrenor2.pokemoni)):
                    if not antrenor2.pokemoni[i-1].este_viu():
                        antrenor2.pokemoni.pop(i-1)
                if not antrenor2.are_pokemoni_vii():
                    print(f'{antrenor2.nume} has no more pokemons.')
                    print(f'{antrenor1.nume} has won!!!')
                    break
                pokemon2 = antrenor2.alege_pokemon()

            pokemon2.ataca(pokemon1)
            print(f'{pokemon2.nume} attacks {pokemon1.nume}, {pokemon1.nume} health: {pokemon1.viata}')

            if not pokemon1.este_viu():
                print(f'{pokemon1.nume} has been defeated!')
                for j in range(len(antrenor1.pokemoni)):
                    if not antrenor1.pokemoni[j-1].este_viu():
                        antrenor1.pokemoni.pop(j-1)
                if not antrenor1.are_pokemoni_vii():
                    print(f'{antrenor2.nume} has no more pokemons.')
                    print(f'{antrenor1.nume} has won!!!')
                    break
                pokemon1 = antrenor1.alege_pokemon()
            if not pokemon1 or not pokemon2:
                break
