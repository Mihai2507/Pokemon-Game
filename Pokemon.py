class Pokemon:
    def __init__(self, nume, tip, viata, putere_atac):
        self.nume = nume
        self.tip = tip
        self.viata = viata
        self.putere_atac = putere_atac

    def ataca(self, alt_pokemon):
        if self.tip == "Apa" and alt_pokemon.tip == "Foc":
            alt_pokemon.viata -= 2 * self.putere_atac
        elif self.tip == "Pamant" and alt_pokemon.tip == "Apa":
            alt_pokemon.viata -= 2 * self.putere_atac
        elif self.tip == "Foc" and alt_pokemon.tip == "Pamant":
            alt_pokemon.viata -= 2 * self.putere_atac
        else:
            alt_pokemon.viata -= self.putere_atac
        if alt_pokemon.viata < 0:
            alt_pokemon.viata = 0  # a murit, deci arata viata 0

    def este_viu(self):
        if self.viata <= 0:
            return False
        else:
            return True

    def __repr__(self):
        return f'{self.nume} --> {self.tip} - Health: {self.viata} and Attack: {self.putere_atac}'
