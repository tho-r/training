voters = {}


def checar_voto(nome):
    if voters.get(nome):
        print("Ja votaste uma vez! Para trás, inimigo da democracia!!!")
    else:
        voters[nome] = True
        print("Vote meu guerreiro do amanhã")


checar_voto("Thomas")
checar_voto("Quinho")
checar_voto("Dih")
checar_voto("Quinho")
