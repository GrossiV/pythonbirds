class Direcao:

    def __init__(self, direcao='Norte'):
        self.direcao = direcao


    def calcular_direcao(self):
        return self.direcao

    def girar_direita(self):
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def girar_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'


if __name__ == '__main__':
    d = Direcao()
    print(d.calcular_direcao())
    d.girar_direita()
    print(d.calcular_direcao())
    d.girar_direita()
    print(d.calcular_direcao())
    d.girar_direita()
    print(d.calcular_direcao())
    d.girar_direita()
    print(d.calcular_direcao())
    d.girar_esquerda()
    print(d.calcular_direcao())
    d.girar_esquerda()
    print(d.calcular_direcao())
    d.girar_esquerda()
    print(d.calcular_direcao())
    d.girar_esquerda()
    print(d.calcular_direcao())
