"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
    cont = 0
    for x in lista:
        if x <= 0:
            cont += 1
            return cont 
            
        
    

def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    # [prof] Faltou o ":" no if (if len(lista) == 0:) e, abaixo, o codigo saiu
    # de dentro da funcao (indentacao zerada), alem de "return []" quando o certo
    # para media de lista vazia e 0. Isso travou o arquivo todo. Original:
    #     if len(lista) == 0
    #     return []
    #      soma = 0
    #     for n in lista:
    #         soma += n
    #     media = soma/len(lista)
    #     return media
    pass


def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    # [prof] Varios erros que derrubaram o arquivo: faltou ":" nos if/for,
    # "Flse" em vez de False, "an" em vez de "and", e o corpo fora da funcao.
    # Revise a indentacao: tudo que e da funcao fica recuado sob o "def".
    # Original (trechos): "if len(lista) == 0" sem ":", "Ja_tirou = Flse",
    # "if n == maior an not Ja_tirou:".
    pass


def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    # [prof] "for i in lista:soma += i" junta duas coisas na mesma linha e o
    # append ficou fora do for. O corpo tambem saiu da funcao. O certo: for na
    # sua linha, corpo recuado. Original:
    #     nova = []
    #     soma = 0
    #     for i in lista:soma += i
    #         nova.append(soma)
    #     return nova
    pass

def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""



# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    # [prof] O corpo saiu de dentro da funcao (indentacao) e o "return" estava
    # dentro do if, o que faria parar na PRIMEIRA ocorrencia, nao na ultima.
    # Para a ultima: percorra tudo, guarde a posicao quando achar e so de return
    # DEPOIS do for. Original:
    #     posicao = -1
    #     for i in range(len(lista)):
    #         if lista[i] == alvo:
    #             posicao = i
    #             return posicao
    pass


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    pass


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    pass


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    pass


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    pass


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    pass


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    pass


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    pass


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    pass


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    pass


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    pass


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    pass


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pass
