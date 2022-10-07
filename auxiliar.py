import time
import random


def encerrarP():
    for i in range(3):
        print("Encerrando em ", 3 - i)
        time.sleep(1)


# ------------------- Sem a tranca -------------------

def contagemR():
    for i in range(10):
        print("R - Contagem Regressiva: ", 10 - i)
        time.sleep(1)


def contagemP():
    for i in range(10):
        print("P - Contagem Progressiva: ", i + 1)
        time.sleep(1)


def geracaoA():
    for i in range(10):
        n = random.randint(1, 100)
        print("A - Numero Aleatorio gerado: ", n)
        time.sleep(1)


# ------------------- Com a tranca -------------------

def l_contagemR(tranca):
    for i in range(10):
        tranca.acquire() # "Tranco" o ponto crítico dessa thread
        print("R - Contagem Regressiva: ", 10 - i)
        tranca.release()  # Desfaço a tranca
        time.sleep(1)



def l_contagemP(tranca):
    for i in range(10):
        tranca.acquire()
        print("P - Contagem Progressiva: ", i + 1)
        tranca.release()
        time.sleep(1)



def l_geracaoA(tranca):
    for i in range(10):
        n = random.randint(1, 100)
        tranca.acquire()
        print("A - Numero Aleatorio gerado: ", n)
        tranca.release()
        time.sleep(1)