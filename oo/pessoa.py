class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'{self.nome} {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def metodo_de_classe(cls):
        # retorna nome atributos de classe
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    frodo = Pessoa(nome='Frodo')
    victor = Pessoa(frodo, nome='Victor')
    print(victor.cumprimentar())
    print(victor.__dict__)
    for filho in victor.filhos:
        print(filho.nome)
        print(filho.olhos)
        print(filho.__dict__)
    print(victor.metodo_estatico())
    print(Pessoa.metodo_estatico())
    print(victor.metodo_estatico())
    print(Pessoa.metodo_de_classe())
    print(victor.metodo_de_classe())

