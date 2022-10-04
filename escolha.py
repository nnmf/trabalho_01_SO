from auxiliar import contagemR, contagemP, geracaoA, encerrarP, l_contagemR, l_contagemP, l_geracaoA
import threading
import time


# Quando estava rodando sem a tranca (Lock), o print vez ou outra vinha com um bug. Para resolver isso implemen-
# tei com a tranca. Porém, resolvi deixar o antigo, portanto, nesse menu tem as duas versões.


def esc(opc):
    match opc:
        case 1:
            esc_noLock()
            return ()
        case 2:
            esc_lock()
            return ()
        case 0:
            encerrarP()
            print("\n----- Programa Encerrado -----")
            return ()
        case default:
            print("Opcao invalida")
            return ()


def esc_noLock():
    # declaro três threads diferentes, cada uma executando uma função diferente
    R = threading.Thread(target=contagemR)
    P = threading.Thread(target=contagemP)
    A = threading.Thread(target=geracaoA)

    # inicio as execuções das threads
    R.start()
    time.sleep(1)
    P.start()
    time.sleep(1)
    A.start()

    # faço com que o programa continue apenas quando todas as execuções acabarem
    R.join()
    P.join()
    A.join()

    print("\n----- Terminado -----\n")


def esc_lock():
    # declaro três threads diferentes, cada uma executando uma função diferente e um objeto tranca(lock) para
    # evitar bug na hora do print. Ao aplicar o objeto lock na função, quando ela chega na hora crítica (na par-
    # te de printar) nós impedimos as outras threads de acessar a sessão até que a tranca seja desfeita. Assim,
    # nós impedimos que o print saia com algum bug.
    tranca = threading.Lock()
    R = threading.Thread(target=l_contagemR, args=(tranca,))
    P = threading.Thread(target=l_contagemP, args=(tranca,))
    A = threading.Thread(target=l_geracaoA, args=(tranca,))

    # inicio as execuções das threads
    R.start()
    P.start()
    A.start()

    # faço com que o programa continue apenas quando todas as execuções acabarem
    R.join()
    P.join()
    A.join()

    print("\n----- Terminado -----\n")
