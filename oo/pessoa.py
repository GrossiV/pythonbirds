class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

    def cumprimentar(self):
        return f'{self.nome} {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Victor')
    print(p.cumprimentar())
