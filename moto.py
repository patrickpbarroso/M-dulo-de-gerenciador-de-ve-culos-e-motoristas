import veiculo

class Moto(veiculo.Veiculo):
    def __init__( self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros


    def abastecer(self, qtd_combustivel):
        print("O método foi chamado a partir da classe moto. ")
        if self._qtd_combustivel >= 30:
            print("Não foi possível abastecer porque a moto já está cheia. ")
        else:
            self._qtd_combustivel += qtd_combustivel

    def pintar(self, cor):
        if cor == "azul":
            print("Não é possível pintar a moto de azul.")
        else:
            self._cor = cor

