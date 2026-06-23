# criador por kiko do ti / ifrs feliz
vida_jogador = 100
vida_monstro = 0
monstro_tag = ""
desejo = 0
loteria = 0
armadura = 0
dano = 0
erro = "=====ERRO.INPUT===="
import random
import os


def explorar_floresta(): #seleção de deseja entrar na floresta 
    while True:
        global desejo
        while desejo !=2 or desejo !=1:
            desejo = int(input("""
        |=======================================|
        | oque deseja fazer ?                   |
        | 1 - entrar na masmorra                |
        | 2 - continuar explorando a floresta   |
        |=======================================|
         >>>"""))
            if desejo == 1:
                print("""
        |=======================================|
        | você entrou na masmorra e olhou em    |
        | volta e não encontrou nenhum inimigo  |
        |=======================================|""")
                explorar_masmorra()
                break
            elif desejo == 2:
                print("""
        |=======================================|
        | você continuo explorando a floresta   |
        | e algumas horas depois encontrou      |
        | outra masmorra                        |
        |=======================================|""")           
            else:
                print(erro)

def explorar_masmorra(): #entrou na masmorra ou ja estava e desejou continuar
    seleção()
    global desejo
    if desejo == 1:
        explorar_floresta()

    elif desejo == 2:
        roleta_russa()

def seleção(): # oque você quer fazer dentro da masmorra
    global desejo
    while desejo !=2 or desejo !=1:
        desejo = int(input("""
        |=======================================|
        | oque deseja fazer ?                   |
        | 1 - sair da masmorra                  |       
        | 2 - entrar mais fundo na masmorra     |
        |=======================================|
         >>>"""))

def roleta_russa():
    global loteria
    loteria = random.choice([1, 2, 3])
    global vida_jogador
    if loteria == 1: #nada
        print("""
        |=======================================|
        | você explorou e não achou nada        |
        |=======================================|""")
        explorar_masmorra()       
        

    elif loteria == 2: #bau
        while desejo !=2 or desejo !=1:
            desejo = int(input("""
        |======================================|
        | você explorou mais fundo e achau um  |
        | bau                                  |
        |======================================|
        | oque deseja fazer?                   |
        | 1 - abrir                            |
        | 2 - ignorar                          |
        |======================================|
         >>>"""))

        if desejo == 1: #abriu o bau
            loteria = random.choice([1, 2])
            if loteria == 1: #nada
                print("""
        |======================================|
        | não tinha nada no bau, oque você     |
        | ira fazer agora?                     |
        |======================================|""")
                explorar_masmorra()
            elif loteria == 2: # poção
                while desejo !=2 or desejo !=1:
                    desejo = int(input("""
        |======================================|
        | dentro havia uma poção suspeita      |
        |======================================|
        | oque você deseja fazer?              |
        | 1 - beber                            |
        | 2 - jogar fora                       |
        |======================================|
         >>>"""))
                if desejo == 1:
                    loteria = random.choice([1, 2, 3])
                    if loteria == 1: # nada
                        print("""
        |======================================|                 
        | ela não possuia nenhum efeito        |
        | provavelmte era so agua suja         |
        |======================================|""")
                        explorar_masmorra()

                    elif loteria == 2: # cura
                        print("""
        |======================================|                 
        | você bebeu ela e sentiu uma energia  |
        | poderosa entrando no seu corpo       |
        | provavelmente essa poção era de      |
        | algum curandeira que ja esteve nesta |
        | masmorra anteriormente               |
        |======================================|""")
                        vida_jogador += 20
                        print(f"""
        |======================================|
        | adicional de vida de: +20            |
        |======================================|
        | vida total: {vida_jogador:<25}        |
        |======================================|""")
                        explorar_masmorra()

                    elif loteria == 3: # azarado do caralho pegou o bagulho envenenado
                        print("""
        |======================================|
        | você bebeu ela e sentiu sua energia  |
        | saindo do seu corpo, ela provavel-   |
        | mente era uma poção envenenada       |
        |======================================|""")
                        vida_jogador -= 20
                        print(f"""
        |======================================| 
        | vida perdida de: -20                 |
        |======================================|
        | vida total: {vida_jogador:<25}|
        |======================================|""")
                        explorar_masmorra()

                    
        elif desejo == 2: # ignorou o bau
            print("""
        |======================================|     
        | você descidiu ignorar o bau e        |
        | continuar explorando                 |
        |======================================| """)
            explorar_masmorra()
        else:
            print(erro)
        
    elif loteria == 3:#monstro escolha
        loteria = random.choice([1, 2, 3])
        global vida_monstro
        global monstro_tag
        if loteria == 1: #slime
            vida_monstro = 100
            monstro_tag = "slime"
        elif loteria == 2: #zumbie
            vida_monstro = 150
            monstro_tag = "zumbie"
        elif loteria == 3: #dragão
            vida_monstro = 300
            monstro_tag = "dragão"
        
        while desejo !=2 or desejo !=1:
            desejo = int(input(f"""
        |======================================|
        | você encontrou um {monstro_tag:<19}|
        | que açao desejo executar?            |
        |======================================|
        | 1 - entrar em combate                |
        | 2 - fugir                            | 
        |======================================|
         >>>"""))
        if desejo == 1: # bora brigar
            print(f"""
        |======================================|    
        | você descidiu entrar em combate com  |
        | {monstro_tag:<37}|
        |======================================|""")    
            combate()
        
        elif desejo == 2: # cagão
            print("""
        |======================================|
        | você fugiu do monstro, e agora que   |
        | ação ira executar?                   | 
        |======================================|""")
            explorar_masmorra()
        else:
            print(erro)

def combate():
    global vida_jogador
    global vida_monstro
    global dano
    while vida_jogador > 0 and vida_monstro > 0:

        print(f"""
        |======================================|
        | monstro: {monstro_tag:<28}|
        | vida:{vida_monstro:<32}|
        |======================================|
        | sua vida: {vida_jogador:<27}|
        |======================================|""")

        while desejo !=2 or desejo !=1:
            desejo = int(input("""
        |======================================|
        | que ação você deseja executar ?      |
        | 1 - atacar                           |
        | 2 - fugir                            |
        |======================================| 
         >>>"""))
        if desejo == 1: # atacar
            print("""
        |======================================|
        | você descidiu atacar                 |
        |======================================|""")
            loteria = random.choice([1, 2, 3])
            if loteria == 1: # errou
                dano = 0

            elif loteria == 2: # normal
                dano = 10

            elif loteria == 3: #critico
                dano = 30
            print(f"""
        |======================================|
        | você infrigiu {dano:<3} de dano            |
        |======================================|""")
            vida_monstro -= dano
            if vida_monstro <= 0:
                print("""
        |======================================|
        | parabens você você derrotou o monstro|
        |======================================|""")
                explorar_masmorra()
            print(f"""
        |======================================|
        | monstro: {monstro_tag:<28}|
        | vida: {vida_monstro:<31}|
        |======================================|
        | agora é o turno do monstro           |
        |======================================|""")

            loteria = random.choice([1, 2, 3])
            if loteria == 1: #errou
                dano = 0

            elif loteria == 2: #normal 
                dano = 10

            elif loteria == 3: # critico
                dano = 30
            print(f"""
        |======================================|
        | ele causou {dano:<3} de dano em você       |
        |======================================|""")
            vida_jogador -= dano
            if vida_jogador <= 0:

                while desejo != 1 or desejo != 2:
                    desejo = int(input("""

        |              GAME__OVER              |    
        |======================================|
        | sua jornada se acaba hoje mas você   |
        | pode voltar a explorar no corpo de   |
        | outro aventureiro corajoso(ou nâo)   |
        |======================================|
        | oque você deseja fazer agora?        |
        | 1 - explorar novamente               |
        | 2 - encerrar jornada                 |
        |======================================|
         >>>"""))
                if desejo == 1:
                    print("""
        |======================================|
        | você iniciou uma nova jornada        |
        |======================================| """)
                    inicio_de_jornada()
                elif desejo == 2:
                    print("""
        |======================================|
        |          obrigado por jogar          |
        |======================================|""")
                    exit()
        elif desejo == 2: #fugir
            centralizado("""
        |======================================|
        | você conseguio fugiu                 |
        |======================================|""")
            seleção()
        else:
            print(erro)

def inicio_de_jornada():
    print("""
        |======================================|
        | você estava explorando a floresta    |
        | e encontrou uma masmorra             |
        |======================================|""")
    explorar_floresta()

while desejo not in (1, 2): # inicio, quando executa o programa
    desejo = int(input("""
        |================ MENU ================|
        | 1 - iniciar jogo                     |
        | 2 - fechar programa                  |
        |======================================|
         >>>"""))
    if desejo not in (1, 2):
        print(erro)
if desejo == 1:
    inicio_de_jornada()
elif desejo == 2:
    print("""
        |======================================|
        | você escolheu fechar o jogo          |
        | espero que jogue novamente mais tarde|
        |======================================|""") 
    exit()       
else:
    print(erro)