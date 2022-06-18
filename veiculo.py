import abc

class Veiculo(abc.ABC):
    """Essa é a classe carro. Essa classe é utilizada para instanciar novos carros em nosso programa"""
    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0


        #Quando um obj

    def __del__(self):
        print("O objeto foi removido da memória. ")

    @abc.abstractmethod
    def pintar(self, cor):
        self.__cor = cor
        print(f"O veículo está com a cor {self.__cor}")
    @property
    def cor(self):
        return self._cor



    def abastecer(self, qtd_combustivel):
        """Esse método é utilizado para abastecer um carro. Ele recebe como parâmetro uma quantidade de combustível e incrementa no atributo qtd_combustivel do objeto carro"""
        self._qtd_combustivel += qtd_combustivel
    #Método que abastece o carro. Ao ser chamado, incrementa 20 unidades na quantidade de combustível armazenado.

    def ligar(self):
        if self.__is_ligado:
            print("O veículo já está ligado.")
        else:
            self.__is_ligado=True
            print("O veículo foi ligado. ")
    #Método que representa o comportamento do carro (elemento da vida real) de ligar.

    def desligar(self):
        if self.__is_ligado == False:
            print("O veículo já está desligado.")
        else:
            self.__is_ligado=False
            print("O veículo foi desligado. ")
    #Método que representa o comportamento do carro (elemento da vida real) de desligar.
    def acelerar(self, velocidade=10):
        if self.__is_ligado==True:
            self.__velocidade += velocidade
        else:
            print("Não é possível acelerar. O veículo está desligado. ")


