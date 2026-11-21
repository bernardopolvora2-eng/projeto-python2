import os
escolha = (input("Digite conta para criar ou tenho para entrar: "))


if escolha == "conta":
    nome = (input("Digite seu nome de usuario: "))
    idade = (input("Digite a sua idade: "))
    senha = (input("dijite a sua senha: "))

    with open("dados.txt", "a") as arquivo:
        arquivo.write(nome + "," + idade + "," + senha + "\n")

    print("Conta criada!")

elif escolha == "tenho":
    nome = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha ")
    encontrou = False

    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
           nome_salvo = linha.split(",")[0]
           senha_salva = linha.strip().split(",")[2]
           if nome_salvo == nome:
             if senha_salva == senha:
                 encontrou = True

    if encontrou:
        print("bem vindo")
        asesso = True
    else:
        print("Usuario nao encontrado ou senha incorreta ")

while True:
    if asesso == True:
     painel = (input("dijite oque entrar calcuradora ou notas ou sair para sair ou excluir a sua conta para escluir dijite a paravra esc: "))

     if painel == "esc":
         esc = (input("voce quer escluir a sua conta? aviso sua conta nao podera ser recuperada! "))
         if esc == "sim":
             os.remove("dados.txt")
             



     
     if painel == "sair":
         break
     
     
     if painel == "calcuradora":
        operasao = (input("dijite o sinal: "))

        numero1 = int(input("dijite o primeiro numero: "))

        numero2 = int(input("dijite o segundo numero: "))

        numero3 = 0

        if operasao == "+":
           numero3 = numero1 + numero2
           print (f"resultado {numero3}")

        if operasao == "*":
           numero3 = numero1 * numero2 
           print (f"resultado {numero3}")

        if operasao == "/":
           numero3 = numero1 / numero2 
           print (f"resultado {numero3}")

        if operasao == "posentagem":
            numero3 = numero1 * numero2 / 100
            print(numero3)

    if  painel == "notas":
        nota_selesoes = (input("que criar uma nota nova ou carregar uma ja feita? , dijite nova para uma nova nota e si quiser carregar dijita carregar ou dijitar excluir para excluir a nota  atual: "))
        if nota_selesoes == "nova":
                   linha1 = (input())
                   linha2 = (input())
                   linha3 = (input())
                   linha4 = (input())
                   linha5 = (input())
                   linha6 = (input())
                   linha7 = (input())
                   linha8 = (input())
                   linha9 = (input())
                   linha10 = (input())
                   with open("notas.txt", "a") as arquivo:
                     arquivo.write(linha1 + "," + linha2 + "," + linha3 + "," + linha4 + "," + linha5 + "," + linha6 + "," + linha7 + "," + linha8 + "," + linha9 + "," + linha10 +"\n")

            
        if nota_selesoes == "carregar":
            with open("notas.txt", "r") as arquivo:
                for linha in arquivo:
                      partes = linha.strip().split(",")
                      print("linha1:", partes[0])
                      print("linha2:", partes[1])
                      print("linha3:", partes[2])
                      print("linha4:", partes[3])
                      print("linha5:", partes[4])
                      print("linha6:", partes[5])
                      print("linha7:", partes[6])
                      print("linha8:", partes[7])
                      print("linha9:", partes[8])
                      print("linha10:", partes[9])
                     
        if nota_selesoes == "excluir":
             remover = (input("deseja excluir o arquivo atual? "))
             if remover == "sim":
                  os.remove("notas.txt")



                   








