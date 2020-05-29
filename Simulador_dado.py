#SEÇÃO DE BIBLIOTECAS
import random, os, PySimpleGUI as sg

#SEÇÃO DE FUNÇÕES
def dadod6():
    #função dado d6
    opt = 1

    os.system('cls') or None
    while opt == 1:
        print("DADO D6")
        opt=int(input('''selecione uma opcao:
        1 - rolar dados
        0 - sair
        opcao: '''))
        if opt == 1:
            os.system('cls') or None
            print("rolando dado!")
            print("numero sorteado foi:")
            num_dado = random.randrange(1,7)
            print(num_dado)
            print('''
            
            ''')         
        elif opt == 0:
           opt = 0
        else:
            print("opcao invalida, tente novamente!")
            dadod6()
    menuprincipal()

def dadod10():
    #função dado d10
    opt = 1

    os.system('cls') or None
    while opt == 1:
        print("DADO D10")
        opt=int(input('''selecione uma opcao:
        1 - rolar dados
        0 - sair
        opcao: '''))
        if opt == 1:
            os.system('cls') or None
            print("rolando dado!")
            print("numero sorteado foi:")
            num_dado = random.randrange(1,11)
            print(num_dado)
            print('''
            
            ''')         
        elif opt == 0:
           opt = 0
        else:
            print("opcao invalida, tente novamente!")
            dadod10()
    menuprincipal()

def dadod20():
    #função dado d20
    opt = 1

    os.system('cls') or None
    while opt == 1:
        print("DADO D20")
        opt=int(input('''selecione uma opcao:
        1 - rolar dados
        0 - sair
        opcao: '''))
        if opt == 1:
            os.system('cls') or None
            print("rolando dado!")
            print("numero sorteado foi:")
            num_dado = random.randrange(1,21)
            print(num_dado)
            print('''
            
            ''')         
        elif opt == 0:
           opt = 0
        else:
            print("opcao invalida, tente novamente!")
            dadod20()
    menuprincipal()

def menuprincipal():
    #função menu principal
    os.system('cls') or None
    opt=int(input('''selecione uma opcao:
    1 - Dado D6
    2 - Dado D10
    3 - Dado D20
    0 - Sair
    opcao: '''))

    if opt == 1:
        dadod6()
    elif opt == 2:
        dadod10()
    elif opt == 3:
        dadod20()
    elif opt == 0:
        os.system('cls') or None
        print("SAINDO DO PROGRAMA!")
        exit()
    else:
        print("opcao invalida, tente novamente!")
        menuprincipal()

#MAIN
#menuprincipal()

sg.theme('DarkBlue')

layout = [
    [sg.Text('SIMULADOR DE DADOS')],
    [sg.Button('Dado D6'), sg.Button('Dado D10'),sg.Button('Dado D20')],
    [sg.Button('cancel')]
]

tela = sg.Window('Simulador de dado by nathan', layout)

while True:
    event, values = tela.read()
    if event in (None, 'cancel'):
        break
    print('voce digitou: ', values[0])
tela.close()