# criador por kiko do ti / ifrs feliz
jogador = {
    "vida": 100,
    "dano": 20,
    "inventario": {
        "armadura": 0,
        "arco": 0,
        "poção_cura": 0,
        "poção_envenenada": 0
        } 
}
monstros = [
    {"nome": "slime", "vida": 100, "dano": 10},
    {"nome": "zumbie", "vida": 150, "dano": 20},
    {"nome": "Dragão", "vida": 200, "dano": 30}
]
desejo = 0
loteria = 0
dano = 0
import random, os, time

def clean():
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

def explorar_floresta(): #seleção de deseja entrar na floresta 
    global desejo
    while True:
        desejo = 0
        while desejo not in (1, 2) :
            try:
                desejo = int(input("""
        |=======================================|
        | oque deseja fazer ?                   |
        | 1 - entrar na masmorra                |
        | 2 - continuar explorando a floresta   |
        |=======================================|
         >>>"""))
            except:
                print("insira um valo valido!")

            if desejo == 1:
                print("""
        |=======================================|
        | você entrou na masmorra e olhou em    |
        | volta e não encontrou nenhum inimigo  |
        |=======================================|""")
                explorar_masmorra()
                
                break
            elif desejo == 2:
                clean()
                print("""
        |=======================================|
        | você continuo explorando a floresta   |
        | e algumas horas depois encontrou      |
        | outra masmorra                        |
        |=======================================|""") 


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
        clean()
        try:
            desejo = int(input("""
        |=======================================|
        | oque deseja fazer ?                   |
        | 1 - sair da masmorra                  |       
        | 2 - entrar mais fundo na masmorra     |
        |=======================================|
         >>>"""))
        except:
            print("insira um valor valido")
def nada(): # nada
    print("""
        |=======================================|
        | você explorou e não achou nada        |
        |=======================================|""")
    desejo = 0
    return    
    

def bau():# ação de achar bau
    global loteria, jogador
    desejo = 0 
    while desejo not in (1, 2):
        try:
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
        except:
            print("insira um valor valido!")

        if desejo == 1: #abriu o bau
            loteria = random.choice([1, 2, 3])
            if loteria == 1: #nada
                print("""
        |======================================|
        | não tinha nada no bau, oque você     |
        | ira fazer agora?                     |
        |======================================|""")
                time.sleep(1)
                return
                
            elif loteria == 2: # poção
                poção_tag = random.choice(["envenenada", "cura"])
                print(f"""
        |======================================|
        | dentro havia uma poção {poção_tag:<14}|
        |======================================|""")
                desejo = 0
                while desejo not in (1, 2, 3):
                    try:
                        desejo = int(input(f"""
        |======================================|
        | oque você deseja fazer?              |
        | 1 - beber                            |
        | 2 - guardar                          |
        | 3 - jogar fora                       |
        |======================================|
         >>>"""))
                    except:
                        print("insira um valor valido")

                if desejo == 1: # beber

                    if poção_tag == "cura": # cura
                        print("""
        |======================================|                 
        | você bebeu ela e sentiu uma energia  |
        | poderosa entrando no seu corpo       |
        | provavelmente essa poção era de      |
        | algum curandeira que ja esteve nesta |
        | masmorra anteriormente               |
        |======================================|""")
                        clean()
                        jogador["vida"] += 20

                        print(f"""
        |======================================|
        | adicional de vida de: +20            |
        |======================================|
        | vida total: {jogador["vida"]:<25}        |
        |======================================|""")
                        clean()
                        return

                    elif poção_tag == "envenenada": # mula tomando o bagulho podre
                        print("""
        |======================================|
        | você bebeu ela e sentiu sua energia  |
        | saindo do seu corpo                  |
        |======================================|""")
                        clean()
                        jogador["vida"] -= 20
                        print(f"""
        |======================================| 
        | vida perdida de: -20                 |
        |======================================|
        | vida total: {jogador["vida"]:<25}|
        |======================================|""")
                        clean()
                        return 
                elif desejo == 2: # guardar
                    jogador["inventario"][f"poção_{poção_tag}"] += 1
                    print(f"""
        |======================================|
        | você achou uma armadura no bau       |
        |======================================|                   
                    """)
                    return
                elif desejo == 3: # jogar fora
                    print(f"""
        |======================================|
        | você jogou fora a poção {poção_tag:<13} |
        |======================================|                     
                    """)
                    return

                else:
                    clean()
            elif loteria == 3: # armadura
                desejo = 0
                print("""
        |======================================|
        | você achou uma armadura no bau       |
        |======================================|""")
                while desejo not in (1, 2, 3):
                    try:
                        desejo = int(input("""
        |======================================|
        | oque deseja fazer ?                  |
        | 1 - equipar                          |
        | 2 - deixar                           |
        |======================================|     
         >>>"""))
                    except:
                        print("insira um valor valido!")

                    if desejo == 1: # equipar
                        if jogador["inventario"]["armadura"] == 0 : # não tem armadura equipada
                            jogador["inventario"]["armadura"] = 1
                            print("""
        |======================================|                   
        | você equipou armadura                |                   
        |======================================|""")
                            return
                        elif jogador["inventario"]["armadura"] == 1:
                            print("""
        |======================================|                   
        | você ja possui armadura equipada     |                   
        |======================================|""")
                            return
                   
                    elif desejo == 2: # deixar
                        print("""
        |======================================|
        | Você deixou a armadura no bau        |
        |======================================|                
                        """)
                        clean
                        return

                    

                    
        elif desejo == 2: # ignorou o bau
            print("""
        |======================================|     
        | você descidiu ignorar o bau e        |
        | continuar explorando                 |
        |======================================| """)
            clean()
            return
        else:
            print(erro)

def achar_monstro():# achar um monstro
    monstro = dict(random.choice(monstros))
        
    desejo = 0
    while desejo not in (1, 2):
        try:
            desejo = int(input(f"""
        |======================================|
        | você encontrou um {monstro["nome"]:<19}|
        | que açao desejo executar?            |
        |======================================|
        | 1 - entrar em combate                |
        | 2 - fugir                            | 
        |======================================|
         >>>"""))
        except:
            print("insira um valor valido!")
        clean()
        if desejo == 1: # bora brigar
            print(f"""
        |======================================|    
        | você descidiu entrar em combate com  |
        | {monstro["nome"]:<37}|
        |======================================|""")
            clean()    
            combate(monstro)
        
        elif desejo == 2: # cagão
            print("""
        |======================================|
        | você fugiu do monstro, e agora que   |
        | ação ira executar?                   | 
        |======================================|""")
            clean()
            return 
        
def roleta_russa():
    global loteria
    loteria = random.choice([1, 2, 3])
    if loteria == 1: #nada
        nada()
        return
        
    elif loteria == 2: #bau
        bau()
        return
       
    elif loteria == 3:#monstro escolha
        achar_monstro()

def combate(monstro):
    global dano, desejo, jogador
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
            try:
                desejo = int(input("""
        |======================================|
        | que ação você deseja executar ?      |
        | 1 - atacar                           |
        | 2 - fugir                            |
        |======================================| 
         >>>"""))
            except:
                print("insira um valor valido!")
            clean()
            if desejo == 1: # atacar
                print("""
        |======================================|
        | você descidiu atacar                 |
        |======================================|""")
                loteria = random.choice([2, 3])

                if loteria == 2: # normal
                    dano = jogador["dano"]

                elif loteria == 3: #critico
                    dano = int(jogador["dano"] * 1.20)
                print(f"""
        |======================================|
        | você infrigiu {dano:<3} de dano            |
        |======================================|""")
                time.sleep(1)
                monstro["vida"] -= dano
                if monstro["vida"] <= 0:
                    print("""
        |======================================|
        | parabens você você derrotou o monstro|
        |======================================|""")
                    time.sleep(1.5)
                    clean()
                    return
                clean()
                print(f"""
        |======================================|
        | monstro: {monstro["nome"]:<28}|
        | vida: {monstro["vida"]:<31}|
        |======================================|
        | agora é o turno do monstro           |
        |======================================|""")
                time.sleep(1)
                loteria = random.choice([1, 2, 3])
                if loteria == 1: #errou
                    dano = 0

                elif loteria == 2: #normal 
                    dano = monstro["dano"]

                elif loteria == 3: # critico
                    dano = int(monstro["dano"] * 1.20)
                
                print(f"""
        |======================================|
        | ele causou {dano:<3} de dano em você       |
        |======================================|""")
                jogador["vida"] -= dano
                if jogador["vida"] <= 0:
                    desejo = 0
                    while desejo not in (1, 2):
                        try:
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
                        except:
                            print("insira um valor valido!")
                        clean()
                    if desejo == 1:
                        print("""
        |======================================|
        | você iniciou uma nova jornada        |
        |======================================| """)
                        clean()
                        inicio_de_jornada()
                    elif desejo == 2:
                        print("""
        |======================================|
        |          obrigado por jogar          |
        |======================================|""")
                        clean()
                        exit()
            elif desejo == 2: #fugir
                print("""
        |======================================|
        | você conseguio fugiu                 |
        |======================================|""")
                clean()
                return
            else:
                print(erro)

def inicio_de_jornada():
    global jogador
    jogador["vida"] = 100
    print("""
        |======================================|
        | você estava explorando a floresta    |
        | e encontrou uma masmorra             |
        |======================================|""")
    explorar_floresta()

while desejo not in (1, 2): # inicio, quando executa o programa
    try:
        desejo = int(input("""
        |================ MENU ================|
        | 1 - iniciar jogo                     |
        | 2 - fechar programa                  |
        |======================================|
         >>>"""))
    except:
        print("porfavor ensira um valor valido")
    clean()
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
    time.sleep(1)
    clean()
    exit()       
else:
    print(erro)