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


if __name__ == '__main__':
    m = Motor()
    print(m.calcular_velocidade())
    m.acelerar()
    print(m.calcular_velocidade())
    m.acelerar()
    m.acelerar()
    print(m.calcular_velocidade())
    m.frear()
    print(m.calcular_velocidade())
    m.frear()
    print(m.calcular_velocidade())
