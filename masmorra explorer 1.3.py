# criador por kiko do ti / ifrs feliz
jogador = {
    "vida": 100,
    "inventario": {"escudo": 0, "arco": 0, "poção": 0} 
}
monstro = {
    "vida": 0,
    "nome": ""
}
desejo = 0
loteria = 0
dano = 0
erro = "=====ERRO.INPUT===="
import random, os, time

def cleam():
    time.sleep(1.2)
    os.system("cls" if os.name == "nt" else "clear")

def explorar_floresta(): #seleção de deseja entrar na floresta 
    global desejo
    while True:
        desejo = 0
        while desejo not in (1, 2) :
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
                cleam()
                print("""
        |=======================================|
        | você continuo explorando a floresta   |
        | e algumas horas depois encontrou      |
        | outra masmorra                        |
        |=======================================|""") 
            else:
                print(erro)

def explorar_masmorra(): #entrou na masmorra ou ja estava e desejou continuar
    global desejo

    while True:
        seleção()

        if desejo == 1:
            return

        elif desejo == 2:
            roleta_russa()

def seleção(): # oque você quer fazer dentro da masmorra
    global desejo
    desejo = 0
    while desejo not in (1, 2):
        cleam()
        desejo = int(input("""
        |=======================================|
        | oque deseja fazer ?                   |
        | 1 - sair da masmorra                  |       
        | 2 - entrar mais fundo na masmorra     |
        |=======================================|
         >>>"""))

def roleta_russa():
    global loteria
    global desejo
    loteria = random.choice([1, 2, 3])
    global jogador
    if loteria == 1: #nada
        print("""
        |=======================================|
        | você explorou e não achou nada        |
        |=======================================|""")
        desejo = 0
        return   
        

    elif loteria == 2: #bau
        desejo = 0 
        while desejo not in (1, 2):
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
                time.sleep(1.5)
                return
                
            elif loteria == 2: # poção
                desejo = 0
                while desejo not in (1, 2):
                    desejo = int(input("""
        |======================================|
        | dentro havia uma poção suspeita      |
        |======================================|
        | oque você deseja fazer?              |
        | 1 - beber                            |
        | 2 - jogar fora                       |
        |======================================|
         >>>"""))

                if desejo == 1: # beber
                    loteria = random.choice([1, 2, 3])
                    if loteria == 1: # nada
                        print("""
        |======================================|                 
        | ela não possuia nenhum efeito        |
        | provavelmte era so agua suja         |
        |======================================|""")
                        cleam()
                        return

                    elif loteria == 2: # cura
                        print("""
        |======================================|                 
        | você bebeu ela e sentiu uma energia  |
        | poderosa entrando no seu corpo       |
        | provavelmente essa poção era de      |
        | algum curandeira que ja esteve nesta |
        | masmorra anteriormente               |
        |======================================|""")
                        cleam()
                        jogador["vida"] += 20

                        print(f"""
        |======================================|
        | adicional de vida de: +20            |
        |======================================|
        | vida total: {jogador["vida"]:<25}        |
        |======================================|""")
                        cleam()
                        return

                    elif loteria == 3: # azarado do caralho pegou o bagulho envenenado
                        print("""
        |======================================|
        | você bebeu ela e sentiu sua energia  |
        | saindo do seu corpo, ela provavel-   |
        | mente era uma poção envenenada       |
        |======================================|""")
                        cleam()
                        jogador["vida"] -= 20
                        print(f"""
        |======================================| 
        | vida perdida de: -20                 |
        |======================================|
        | vida total: {jogador["vida"]:<25}|
        |======================================|""")
                        cleam()
                        return 
                else:
                    cleam()

                    
        elif desejo == 2: # ignorou o bau
            print("""
        |======================================|     
        | você descidiu ignorar o bau e        |
        | continuar explorando                 |
        |======================================| """)
            cleam()
            return
        else:
            print(erro)
        
    elif loteria == 3:#monstro escolha
        loteria = random.choice([1, 2, 3])
        global monstro
        if loteria == 1: #slime
            monstro["vida"] = 100
            monstro["nome"] = "slime"
        elif loteria == 2: #zumbie
            monstro["vida"] = 150
            monstro["nome"] = "zumbie"
        elif loteria == 3: #dragão
            monstro["vida"] = 300
            monstro["nome"] = "dragão"
        
        desejo = 0
        while desejo not in (1, 2):
            desejo = int(input(f"""
        |======================================|
        | você encontrou um {monstro["nome"]:<19}|
        | que açao desejo executar?            |
        |======================================|
        | 1 - entrar em combate                |
        | 2 - fugir                            | 
        |======================================|
         >>>"""))
        cleam()
        if desejo == 1: # bora brigar
            print(f"""
        |======================================|    
        | você descidiu entrar em combate com  |
        | {monstro["nome"]:<37}|
        |======================================|""")
            cleam()    
            combate()
        
        elif desejo == 2: # cagão
            print("""
        |======================================|
        | você fugiu do monstro, e agora que   |
        | ação ira executar?                   | 
        |======================================|""")
            cleam()
            return 
        else:
            print(erro)

def combate():
    global jogador
    global monstro
    global dano
    global desejo
    while jogador["vida"] > 0 and monstro["vida"] > 0:

        print(f"""
        |======================================|
        | monstro: {monstro["nome"]:<28}|
        | vida:{monstro["vida"]:<32}|
        |======================================|
        | sua vida: {jogador["vida"]:<27}|
        |======================================|""")

        desejo = 0
        while desejo not in (1, 2):
            desejo = int(input("""
        |======================================|
        | que ação você deseja executar ?      |
        | 1 - atacar                           |
        | 2 - fugir                            |
        |======================================| 
         >>>"""))
            cleam()
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
                time.sleep(1.5)
                monstro["vida"] -= dano
                if monstro["vida"] <= 0:
                    print("""
        |======================================|
        | parabens você você derrotou o monstro|
        |======================================|""")
                    time.sleep(1.5)
                    cleam()
                    return
                cleam()
                print(f"""
        |======================================|
        | monstro: {monstro["nome"]:<28}|
        | vida: {monstro["vida"]:<31}|
        |======================================|
        | agora é o turno do monstro           |
        |======================================|""")
                time.sleep(2)
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
                jogador["vida"] -= dano
                if jogador["vida"] <= 0:
                    desejo = 0
                    while desejo not in (1, 2):
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
                        cleam()
                    if desejo == 1:
                        print("""
        |======================================|
        | você iniciou uma nova jornada        |
        |======================================| """)
                        cleam()
                        inicio_de_jornada()
                    elif desejo == 2:
                        print("""
        |======================================|
        |          obrigado por jogar          |
        |======================================|""")
                        cleam()
                        exit()
            elif desejo == 2: #fugir
                print("""
        |======================================|
        | você conseguio fugiu                 |
        |======================================|""")
                cleam()
                return
            else:
                print(erro)

def inicio_de_jornada():
    jogador["vida"] = 100
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
    cleam()
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
    time.sleep(1.5)
    cleam()
    exit()       
else:
    print(erro)