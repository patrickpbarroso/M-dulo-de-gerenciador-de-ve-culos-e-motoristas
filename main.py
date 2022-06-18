import motorista, carro, moto

continuar = 1
i = -1 #índice que será incrementado e usado para associar motorista a veiculo
carros = []
motos = []
motoristas = []

while continuar == 1:
#Menu inicial
    n = int(input("------Menu------"
                  "\n(1) Registrar veículo"
                  "\n(2) Registrar motorista"))
    #Menu secundário para quem quiser registrar veículo (Apertar 1 no menu inicial)
    if n == 1:
        j = int(input("------Adicionar Veículo------"
                  "\n(1) Carro"
                  "\n(2) Moto"))
        #Caso o veículo a se cadastrar seja um carro
        if j == 1:
            print("------Adicionar Carro------")
            cor = input("Cor do carro: ")
            combustivel = input("Tipo de combustível: ")
            potencia = input("Potência do carro: ")
            portas = int(input("Quantidade de portas: "))

            continuar = int(input("Digite (1) para continuar no sistema e (0) para sair"))

            carros.append(carro.Carro(cor,combustivel,potencia,portas))
        #Caso o veículo a se cadastrar seja uma moto
        if j == 2:
            print("------Adicionar Moto------")
            cor = input("Cor da moto: ")
            combustivel = input("Tipo de combustível: ")
            potencia = float(input("Potência da moto: "))
            passageiros = int(input("Quantidade de passageiros da moto:"))

            continuar = int(input("Digite (1) para continuar no sistema e (0) para sair"))

            motos.append(moto.Moto(cor, combustivel, potencia, passageiros))

    #Caso a pessoa selecione 2 (registrar motorista) no menu inicial

    if n==2:
        i += 1
        print("------Adicionar Motorista------")
        nome = input("Nome: ")
        cpf = int(input("Cpf: "))
        habilitacao = input("Habilitação: ")
        motoristas.append(motorista.Motorista(nome, cpf, habilitacao))

        continuar = int(input("Digite (1) para continuar no sistema e (0) para sair"))









    #motorista1 = motorista.Motorista("Patrick", 21591, 22)
    #uno_verde = carro.Carro("preto", "flex", 2.0, 4)


