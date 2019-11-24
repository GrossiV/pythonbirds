class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0

    def calcular_velocidade(self):
        return self.velocidade


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


class Carro:

    def __init__(self, motor, direcao):
        self.direcao = direcao
        self.motor = motor


    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_esquerda(self):
        return self.direcao.girar_esquerda()

    def girar_direita(self):
        return self.direcao.girar_direita()
