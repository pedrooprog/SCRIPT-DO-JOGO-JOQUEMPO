#----------SCRIPT: JOGO JOQUEMPÔ-------------#

from random import randint
from time import sleep
from sys import exit

def joquempo():
    while True:
        try:
            lista = ['papel', 'tesoura', 'pedra']
            print('[0] papel')
            print('[1] tesoura')
            print('[2] pedra')
            print('[9] Para o programa')
            print('Qual intem você vai jogar?')
            resp = int(input('>>'))

            if resp == 9:
                print('\033[1:36mTchau!!!, Até a proxima!!!\033[m')
                exit()
            print("JO\n")
            sleep(1)
            print("KEN\n")
            sleep(1)
            print("POOH!!!\n")
            computador = randint(0,2)
            print('\033[1:36m-\033[m'*30)
            print(f"O computador escolheu: \033[1:31m{lista[computador]}\033[m")
            print(f"O jogador escolheu: \033[1:33m{lista[resp]}\033[m")
            print('\033[1:36m-\033[m' * 30)



            if computador == 0:
                if resp == 1:
                    print("\033[1:31mEmpate!\033[m")
                elif resp == 2:
                    print("\033[1:31mJogador perdeu\033[m")
                elif resp == 3:
                    print("\033[1:31mComputador venceu\033[m")
                else:
                    print('Comando invalido')


            elif computador == 1:
                if resp == 1:
                    print("\033[1:31mComputador venceu\033[m")
                elif resp == 2:
                    print("\033[1:31mEmpate!\033[m")
                elif resp == 3:
                    print("\033[1:31mJogador perdeu\033[m")
                else:
                    print('Comando invalido')

            elif computador == 2:
                if resp == 1:
                    print("\033[1:31mJogador perdeu\033[m")
                elif resp == 2:
                    print("\033[1:31mComputador venceu\033[m")
                elif resp == 3:
                    print("\033[1:31mEmpate!\033[m")
                else:
                    print("Operacao invalida")
            else:
                print("Operacao invalida")


            print('Deseja jogar novamente?')
            while True:
                r = str(input('>>'))[0].strip().upper()
                if r in 'SN':
                    break
                print('\033[1:31mPor Favor digite apenas Sim ou Não\033[m')
            if r == 'N':
                print('\033[1:36mAté a proxima!!!')
                break
        except(ValueError,TabError,IndexError):
            print('\033[1:31mCOMANDO INVALIDO\033[m')
            continue


