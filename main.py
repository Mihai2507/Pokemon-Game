from Pokemon import Pokemon
from Antrenor import Antrenor
from Batalie import Batalie


def main():
    name1 = input("Hello!\nWhat is your gamer names?\n")
    name2 = input("Ok. And yours?\n")
    while name1 == "" or name2 == "":
        name1 = input("ERROR. Please enter your gamer name again.\n")

    print(f'Hello, {name1} and {name2}')
    batalie = Batalie()
    start = input("Would you like to start?\nY/N\n")
    if start == "Y" or start == "y":
        Bulbasaur = Pokemon("Bulbasaur", "Grass", 100, 20)
        Venusaur = Pokemon("Venusaur", "Grass", 110, 22)
        Ivysaur = Pokemon("Ivysaur", "Grass", 115, 24)
        Blastoise = Pokemon("Blastoise", "Water", 120, 18)
        Wartortle = Pokemon("Wartortle", "Water", 130, 15)
        Squirtle = Pokemon("Squirtle", "Water", 125, 17)
        Charmeleon = Pokemon("Charmeleon", "Fire", 95, 24)
        Charmander = Pokemon("Charmander", "Fire", 100, 23)
        Charizard = Pokemon("Charizard", "Fire", 90, 25)

        antrenor1 = Antrenor("Red", [Bulbasaur, Blastoise, Charmander])
        antrenor2 = Antrenor("Chase", [Charmeleon, Squirtle, Ivysaur])
        antrenor3 = Antrenor("Ethan", [Venusaur, Wartortle, Charizard])
        print("First of all, you must choose a trainer to fight with.\nYou can choose between Red, "
              "Chase and Ethan.\n")
        print(antrenor1)
        print(antrenor2)
        print(antrenor3)
        trainer = input("Who is going to be your choice?\n")
        adversar = input("And which one will you fight against?\n")

        if trainer == "Red" and adversar == "Chase":
            batalie.lupta(antrenor1, antrenor2)
            print("\nThe final state of the pokemons:")
            print(antrenor1)
            print(antrenor2)
        elif trainer == "Red" and adversar == "Ethan":
            batalie.lupta(antrenor1, antrenor3)
            print("\nThe final state of the pokemons:")
            print(antrenor1)
            print(antrenor3)
        elif trainer == "Chase" and adversar == "Red":
            batalie.lupta(antrenor2, antrenor1)
            print("\nThe final state of the pokemons:")
            print(antrenor2)
            print(antrenor1)

        elif trainer == "Chase" and adversar == "Ethan":
            batalie.lupta(antrenor2, antrenor3)

            print("\nThe final state of the pokemons:")
            print(antrenor2)
            print(antrenor3)

        elif trainer == "Ethan" and adversar == "Red":
            batalie.lupta(antrenor3, antrenor1)

            print("\nThe final state of the pokemons:")
            print(antrenor3)
            print(antrenor1)

        elif trainer == "Ethan" and adversar == "Chase":
            batalie.lupta(antrenor3, antrenor2)

            print("\nThe final state of the pokemons:")
            print(antrenor3)
            print(antrenor2)

    elif start == "N" or start == "n":
        print(f'Ok, guys. I will see you later!')
        exit(1)


if __name__ == "__main__":
    main()
