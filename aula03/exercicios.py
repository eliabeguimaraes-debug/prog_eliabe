"""Aula 03 - Construa e diga o custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

ATENCAO: quase todas as funcoes desta aula devolvem DUAS coisas,
o resultado e a contagem de operacoes:

    return soma, operacoes

Quem devolve so o resultado nao passa nos testes.
"""


def soma_contando(lista):
    """Devolve (soma, operacoes).
    Conte 1 operacao para cada numero que voce somar.
    soma_contando([1, 2, 3]) -> (6, 3)"""
    pass
def soma_contando(lista)
    soma = 0
    ops = 0
    for x in lista: 
        soma += x
        ops += 1
    return soma, ops

def busca_linear_contando(lista, alvo):
    """Devolve (posicao, comparacoes), ou (-1, comparacoes) se nao achar.
    Conte 1 comparacao cada vez que comparar um elemento com o alvo.
    Pare assim que encontrar."""
    pass
    def busca_linear_contando(lista, alvo):
        comp = 0
        for i, v in enumerate(lista):
            comp += 1
            if v == alvo:
                return i, comp
        return -1, comp


def busca_binaria_contando(lista, alvo):
    """Recebe uma lista JA ORDENADA.
    Devolve (posicao, comparacoes), ou (-1, comparacoes) se nao achar.
    Conte 1 comparacao cada vez que olhar o elemento do meio."""
    pass
def busca_binaria_contando(lista, alvo):

    ini, fim = 0, len(lista) - 1
    comp = 0
    while ini <= fim:
        meio = (ini + fim) // 2
        comp += 1
        if lista[meio] == alvo:
            return meio, comp
        elif lista[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1, comp

def tem_repetido_contando(lista):
    """Devolve (True, comparacoes) ou (False, comparacoes).
    Conte 1 comparacao cada vez que comparar um par de elementos.
    Pare assim que encontrar o primeiro repetido."""
    pass
def tem_repitido_contando(lista):
    comp = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)): 
            comp += 1
            if lista[i] == lista[j];
            return True, comp
    return False, comp

def quantas_divisoes(n):
    """Quantas vezes da para dividir n por 2 ate sobrar 1.
    Use divisao inteira. Devolve so o numero, sem contagem.
    quantas_divisoes(8) -> 3"""
    pass
def quantas_divisoes(n):

c = 0
while n > 1:
    n //= 2
    c == 1
    return c

def mais_frequente_contando(lista):
    """(Desafio) Devolve (valor, comparacoes).
    O valor que mais aparece na lista. Em caso de empate, o que aparece
    primeiro. Conte 1 comparacao cada vez que comparar dois elementos."""
    pass
def mais_frequente_contando(lista):

    if not lista:
        return None, 0

comp = 0
mais_freq = lista[0]
max_qtd = 0

for i in range(len(lista)):

    ja_visto + False
    for k in range(i):
        comp += 1]if lista[k] == lista[i]:
            ja_visto = True
            if ja_visto = True]break
            if ja_visto:
                continue

            qtd = 0
            for j in range (len(lista)):
                comp += 1
                if lista[j] == lista[i]:
                    qtd += 1

            if qtd > max_qtd:
                max_qtd = qyd
                mais_freq= lista[i]

    return mais_freq, comp
