import pessoa

class Motorista(pessoa.Pessoa):

    def __init__(self, nome, cpf, habilitacao):
        super().__init__(nome, cpf)
        self.__habilitacao = habilitacao



    @property
    def habilitacao(self):
        return self.__habilitacao






