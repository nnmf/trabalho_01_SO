from escolha import esc

# Programa rodado com python versão 3.10.7

# O programa é bem simples. No auxiliar tem três funções, uma faz uma contagem regressiva, outra faz uma
# contagem progressiva e a última gera números aleatórios de 1 a 100. O programa roda os três em simultâneo,
# o que diferencia são as letras no começo dos prints: R - Contagem Regressiva, P - Contagem Progressiva e
# A - Geração Aleatória de Números.

if __name__ == '__main__':
    print("----- Programa Iniciado -----\n")
    op=1
    while op!=0:
        op = input("Selecione uma das opcoes abaixo:\n1 - Threading sem a tranca\n2 - Threading com a tranca\n0 - "
                   "Sair\nEscolha: ")
        op = int(op)
        esc(op)