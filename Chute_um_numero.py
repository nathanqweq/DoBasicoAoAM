# Jogo recriado por Nathan Quadros da Silva
# Contatos:
#   contato@nathanqsilva.com.br
#   contato@cafecomnoc.website
# Visite:
#   nathanqsilva.com.br
#   cafecomnoc.website
#
#
#
#OBSERVAÇÕES
# O codigo está feito para ser executado em maquinas windows devido ao comando cls
# O codigo será executado normalmente no linux mas o comando os.system não fara a limpeza da tela
# Para corrigir basta alterar todas as aparições de 'cls' para 'clear'

#BIBLIOTECAS
import random, os

#VARIAVEIS GLOBAIS
dificuldade = 2

#FUNÇÕES
def menuprincipal():
    os.system('cls') or None
    opt = int(input('''Bem vindo ao chute um numero:
    digite uma das opcoes:
    1 - Jogar
    2 - Opcoes
    0 - sair
    opção: '''))

    if opt == 1:
        jogar()
    elif opt == 2:
        menu_opt()
    elif opt == 0:
        exit()
    else:
        menuprincipal()

def jogar():
    os.system('cls') or None
    global dificuldade
    num_esc = 0
    if dificuldade == 1:
        num_sec = random.randrange(1,11)
    elif dificuldade == 2:
        num_sec = random.randrange(1,101)
    elif dificuldade == 3:
        num_sec = random.randrange(1,1001)
    
    mostra_dificuldade()
    while num_sec != num_esc:
        print("digite um numero aleatorio")
        num_esc = int(input("numero: "))
        if num_esc < num_sec:
            print("chutou baixo!")
        elif num_esc > num_sec:
            print("chutou alto!")
    os.system('cls') or None
    print("parabens voce ganhou o numero escolhido era", num_sec)
    print("precione enter para voltar ao menu principal!")
    os.system('pause')
    menuprincipal()   

def mostra_dificuldade():
    global dificuldade
    if dificuldade == 1:
        print("deficuldade atual e facil! (1 - 10)")
    elif dificuldade == 2:
        print("dificuldade atual e medio! (1 - 100)")
    elif dificuldade == 3:
        print("dificuldade atual e dificil! (1 - 1000)")

def menu_opt():
    global dificuldade
    os.system('cls') or None
    opt = int(input('''selecione uma opcao:
    1 - selecionar dificuldade
    0 - sair
    opcao: '''))
    if opt == 1:
        os.system('cls') or None
        print("OPÇÕES!")
        print('''selecione uma dificuldade
        1 - Facil (1 - 10)
        2 - Medio (1 - 100)
        3 - dificil (1 - 1000)''')
        mostra_dificuldade()
        dificuldade = int(input("opcao: "))
        menuprincipal()

    elif opt == 0:
        menuprincipal()

    else:
        print("erro, opcao errada tente novamente")
        menu_opt()    
    

#MAIN
menuprincipal()