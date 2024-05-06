import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos"""
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r"[.!?]+", texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r"[,:;]+", sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """Essa função recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas."""
    similaridade_total = 0
    for i in range(len(as_a)):
       similaridade_total += abs(as_a[i] - as_b[i]) / 6

    return similaridade_total / len(as_a)


    
    


def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    palavras = []
    for s in sentencas:
        palavras += separa_palavras(s)
    tam_medio_palavra = tamanho_medio_palavras(palavras)
    rel_type_token = n_palavras_diferentes(palavras) / len(palavras)
    hapax_legomana = n_palavras_unicas(palavras) / len(palavras)
    tam_medio_sentenca = tamanho_medio_sequencia(sentencas)
    complexidade_sentenca = complexidade__de_sequencia(sentencas, palavras)
    tam_medio_frase = tamanho_medio__de_frase(sentencas, palavras)

    return [tam_medio_palavra, rel_type_token, hapax_legomana, tam_medio_sentenca, complexidade_sentenca, tam_medio_frase]

def avalia_textos(textos, ass_cp):
    """Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH."""
    similaridades = [compara_assinatura(ass_cp, calcula_assinatura(texto)) for texto in textos]
    texto_infectado = similaridades.index(min(similaridades)) + 1
    return texto_infectado



def tamanho_medio__de_frase(txt, lst_frase):
    a = 0

    for i in txt:
        a += len(i)

    return a / len(lst_frase)


def complexidade__de_sequencia(txt, frases):
    return len(frases) / len(txt)


def tamanho_medio_sequencia(txt):
    tam = 0

    for i in txt:
        tam += len(i)

    return tam / len(txt)


def tamanho_medio_palavras(palavras):
    med = 0
    tam = 0
    for i in palavras:
        tam += len(i)

    return tam / len(palavras)


if __name__ == "__main__":

    as_a = le_assinatura()
    textos = le_textos()

    texto_infectado = avalia_textos(textos, as_a)

    print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH.")