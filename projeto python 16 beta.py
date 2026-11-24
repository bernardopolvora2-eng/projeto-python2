#bliotecas
import os
import time
import winsound
from PIL import Image # type: ignore

#disonario onde diz as paravras que sao a mesma coisa
help = {
"help": ["socorro", "ajuda", "manual"],
"ajuda": ["help", "manual", "socorro"],
"manual": ["socorro", "ajuda","help"],
"socorro": ["manual", "ajuda", "healp"]

}




#verifica se voce tem ou nao uma conta
asesso = False
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
    asesso = True
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
     painel = (input("digite oque entrar calcuradora ou notas cronometro ou sair para sair ou excluir a sua conta para excluir digite a paravra esc: ")).lower()

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
         tempo_real = tempo * 3600
         for i in range(tempo_real, 0, -1):
             print(f"Faltam {i} segundos")
             time.sleep(1)
         print ("tempo esgotado!")
         winsound.MessageBeep()

    #verifica se foi digitado no painel help ou ajuda e outras palavras
    if painel in help:
        print ("ben vindo ao manual de instrusoes ")
        print ("ese aplicativo e um aplicativo mute funsional temos muitas coisas, calcuradora notas cronometro tudo iso no aplicativo" \
        "para asesar os aplicativos e so digitar oque voce quer no painel ")
        time.sleep(60)
        help_sair = (input("digite sair para sair do manual: "))

        #modo pixel para desenhar com letras ou pontos e salvar em uma imagem (modo secreto)
    if painel == "pixel":
        modo = input("Modo (letras, ponto ou pronto): ").strip().lower()

        cores = {
          ".": (255, 255, 255),
            "P": (0, 0, 0),
            "V": (255, 0, 0),
            "A": (0, 0, 255),
            "Y": (255, 255, 0),
            "G": (0, 160, 0),
            "L": (255, 128, 0),
        }

        linhas = []

        if modo == "letras":
            print("Letras:", " ".join(cores))
            print("Digite uma linha de letras (ex: VVGGAA). Enter vazio termina.")
            print (". = branco, P = preto, V = vermelho, A = azul, Y = amarelo, G = verde, L = laranja")
            nome = input("Digite o nome do desenho: ")
            while True:
                linha = input(f"Linha {len(linhas) + 1}: ").strip().upper()
                if linha == "":
                    break
                if any(letra not in cores for letra in linha):
                    print("Letra invalida. Use:", " ".join(cores))
                    continue
                linhas.append(linha)

        elif modo == "ponto":
            largura = int(input("Largura: "))
            altura = int(input("Altura: "))
            grade = [["."] * largura for _ in range(altura)]
            print("Digite: x y letra (ex: 3 2 V). Enter vazio termina.")
            while True:
                entrada = input("> ").strip().upper().split()
                if not entrada:
                    break
                if len(entrada) != 3 or not entrada[0].isdigit() or not entrada[1].isdigit():
                    print("Formato: x y letra")
                    continue
                x, y, letra = int(entrada[0]), int(entrada[1]), entrada[2]
                if letra not in cores or x >= largura or y >= altura:
                    print("Letra ou posicao invalida.")
                    continue
                grade[y][x] = letra
                for l in grade:
                    print(" ".join(l))
            linhas = ["".join(l) for l in grade]
            #. = branco , P = preto, V = vermelho, A = azul, Y = amarelo, G = verde, L = laranja

        elif modo == "pronto":
            select_pixel_pront =  (input("que desenho voce quer?"))
            if select_pixel_pront == "arvore":
             linhas = [
                "AAAAAAAAAA",
                "AAAYYYYAAA",
                "AAYYYYYYAA",
                "AAGGYYAAA",
                "AGGGGAAAA",
                "AALLAAAAAA",
                "AALLAAAAAA",
                "GGGGGGGGGG",
             ]
            if select_pixel_pront == "casa":
                 linhas = [
                "AAAAAAAAAA",
                "AAAAYYAAAA",
                "AAAYYYYAAA",
                "AVVVVVVAAA",
                "VVVVVVVVAA",
                "ALLYYLLAAA",
                "ALLYYLLAAA",
                "GGGGGGGGGG",
             ]
            if select_pixel_pront == "montanha":
                   linhas = [
                "YYYAAAAAAA",
                "YYAAALVVAA",
                "AAAAALAAVA",
                "AAAA..AAAA",
                "AAA....AAA",
                "AAGGGGGGAA",
                "AGGGGGGGGA",
                "GGGGGGGGGG",
             ]
            nome = "desenho pre definido"
        else:
            print("Modo nao existe.")

        if linhas:
            altura = len(linhas)
            largura = max(len(l) for l in linhas)
            img = Image.new("RGB", (largura, altura), (255, 255, 255))
            for y, linha in enumerate(linhas):
                for x, letra in enumerate(linha):
                    img.putpixel((x, y), cores[letra])
            img = img.resize((largura * 30, altura * 30), Image.Resampling.NEAREST)
            img.save(f"{nome}.png")
            print(f"Imagem salva em {nome}.png")