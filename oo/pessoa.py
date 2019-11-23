class Pessoa:
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'{self.nome} {id(self)}'


if __name__ == '__main__':
    frodo = Pessoa(nome='Frodo')
    victor = Pessoa(frodo, nome='Victor')
    print(victor.cumprimentar())

    for filho in victor.filhos:
        print(filho.nome)
