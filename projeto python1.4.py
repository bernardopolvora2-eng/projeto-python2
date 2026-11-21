#bliotecas
import os
import time
import winsound

#verifica se voce tem ou nao uma conta 
escolha = (input("Digite conta para criar ou tenho para entrar: "))

#criar conta
if escolha == "conta":
    nome = (input("Digite seu nome de usuario: "))
    idade = (input("Digite a sua idade: "))
    senha = (input("digite a sua senha: "))
 #cria um arquivo de testo com os dados
    with open("dados.txt", "a") as arquivo:
        arquivo.write(nome + "," + idade + "," + senha + "\n")

    print("Conta criada!")
 #verifica se tem o arquivo de testo com os dados
elif escolha == "tenho":
    nome = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha ")
    encontrou = False
 #verifica se os dados estao sertos 
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
 #abre o painel para escrever oque quer entrar
while True:
    if asesso == True:
     painel = (input("digite oque entrar calcuradora ou notas cronometro ou sair para sair ou excluir a sua conta para excluir digite a paravra esc: "))

     if painel == "esc":
         esc = (input("voce quer excluir a sua conta? aviso sua conta nao podera ser recuperada! "))
         if esc == "sim":
             os.remove("dados.txt")
             



     #verifica se digitou sair 
     if painel == "sair":
         break
     
     #verifica se digitou calcuradora e abre a calcuradora
     if painel == "calcuradora":
        operasao = (input("digite o sinal: "))

     #calcura os numeros digitados
        numero1 = int(input("digite o primeiro numero: "))

        numero2 = int(input("digite o segundo numero: "))

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
     #verifica se foi escrito a palavra notas
    if  painel == "notas":
        nota_selesoes = (input("que criar uma nota nova ou carregar uma ja feita? , digite nova para uma nova nota e si quiser carregar digita carregar ou digitar excluir para excluir a nota  atual: "))
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
                    # cria um arquivo com as linhas da nota
                   with open("notas.txt", "a") as arquivo:
                     arquivo.write(linha1 + "," + linha2 + "," + linha3 + "," + linha4 + "," + linha5 + "," + linha6 + "," + linha7 + "," + linha8 + "," + linha9 + "," + linha10 +"\n")

         #verifica se a palavra carregar foi dijitada no notas_selesoes  e abre o arquivo da notas e escre ele no terminal 
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
         #exclui o arquivo da notas            
        if nota_selesoes == "excluir":
             remover = (input("deseja excluir o arquivo atual? "))
             if remover == "sim":
                  os.remove("notas.txt")


    # cronometra o tempo em segundos e quando termina toca um som
    if painel == "cronometro":
        cronometro_select = (input("digite a medida de tempo segundos , minutos , horas: "))

        if cronometro_select == "segundos":
         
         tempo = int(input("digite o tempo:"))
         for i in range(tempo, 0, -1):
              print(f"Faltam {i} segundos")
              time.sleep(1)
         print ("tempo esgotado!")
         winsound.MessageBeep()

        if cronometro_select == "minutos":

         tempo = int(input("digite o tempo:"))
         tempo_real = tempo * 60
         for i in range(tempo_real, 0, -1):
            print(f"Faltam {i} segundos")
            time.sleep(1)
         print ("tempo esgotado!")
         winsound.MessageBeep()

        if cronometro_select == "horas":
         tempo = int(input("digite o tempo:"))
         tempo_real = tempo * 120
         for i in range(tempo_real, 0, -1):
             print(f"Faltam {i} segundos")
             time.sleep(1)
         print ("tempo esgotado!")
         winsound.MessageBeep()


             

    
    
    




                   








