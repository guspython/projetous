class Personagem:
    def __init__(self, nome, poder, raca, dmg):
        self.nome = nome
        self.poder = poder
        self.lista_racas = ["Humano", "Mink", "Elfo"]
        if raca in self.lista_racas:
            self.raca = raca
        else:
            print("Erro. Escolha raça corretamente")

        self.dmg = dmg

    def possui_raca(self):
        if self.raca:
            self.dmg += 2
            return True
        return False


p1 = Personagem("Gustavo", "Fogo", "Humano", 10)
p2 = Personagem("Pedro", "Água", "Ork", 10)
p1.possui_raca()
p2.possui_raca()

print(f"{p1.nome} possui a raça:{p1.raca}\nDano:{p1.dmg}")
print(f"{p2.nome} possui a raça:{p2.raca}\nDano:{p2.dmg}")