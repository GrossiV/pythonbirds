class Direcao:

    def __init__(self, valor='Norte'):
        self.valor = valor


    def calcular_direcao(self):
        return self.valor

    def girar_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'

    def girar_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'


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
