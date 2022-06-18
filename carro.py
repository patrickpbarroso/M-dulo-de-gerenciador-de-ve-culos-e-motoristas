import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel,potencia)  #Atributos herdados da classe pai (veículo)
        self.qtd_portas = qtd_portas

        #Atributo específico da classe filha (carro)
    
    def abastecer(self, qtd_combustivel):
        print("O método foi chamado a partir da classe carro. ")
        self._qtd_combustivel += qtd_combustivel

    def pintar(self, cor):
        if cor == "preto":
            print("Não é possível pintar o carro de preto. ")
        else:
            self._cor = cor
