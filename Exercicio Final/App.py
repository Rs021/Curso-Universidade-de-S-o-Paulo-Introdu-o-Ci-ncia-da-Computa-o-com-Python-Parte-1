import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos"""
    #print("Bem-vindo ao detector automático de COH-PIAH.")
    #print("Informe a assinatura típica de um aluno infectado:")

    wal = 4.51  # float(input("Entre o tamanho médio de palavra:"))
    ttr = 0.693  # float(input("Entre a relação Type-Token:"))
    hlr = 0.55  # float(input("Entre a Razão Hapax Legomana:"))
    sal = 70.82  # float(input("Entre o tamanho médio de sentença:"))
    sac = 1.82  # float(input("Entre a complexidade média da sentença:"))
    pal = 38.2  # float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
   # i = 1
    textos = ['Olá', 'Gostamos de voces']
    #texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    #while texto:
     #   textos.append(texto)
    #    i += 1
    #    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

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
    """IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas."""

    similaridade = 0
    sim = 0

    print(as_b)


    


def calcula_assinatura(texto):
    # texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
    """IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto."""

    """Tamanho médio de palavra é a soma dos tamanhos das 
    palavras dividida pelo número total de palavras"""

    """[4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]"""

    senteca = separa_sentencas(texto)

    lista_palavras = []

    for i in senteca:
        frases = separa_frases(i)

        for j in frases:
            lista_palavras.append(j)

    separadas = []

    for i in lista_palavras:
        sep = separa_palavras(i)
        for k in sep:
            separadas.append(k)

    tam_medio = tamanho_medio_palavras(separadas)
    razao_token_type = n_palavras_diferentes(separadas) / len(separadas)
    razao_hepax_logomana = n_palavras_unicas(separadas) / len(separadas)
    tamanho_medio_setenca = tamanho_medio_sequencia(senteca)
    complexidade_de_sentenca = complexidade__de_sequencia(senteca, lista_palavras)
    tamanho_medio_frase = tamanho_medio__de_frase(lista_palavras, lista_palavras)

    dc = (
        tam_medio,
        razao_token_type,
        razao_hepax_logomana,
        tamanho_medio_setenca,
        complexidade_de_sentenca,
        tamanho_medio_frase,
    )
    return dc


def avalia_textos(textos, ass_cp):
    """IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH."""

    pass


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
    texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

    as_a = le_assinatura()
    textos = [texto, 'ryan', 'Ruan']


    calc_ast = []

    for j in textos:
        calc_ast.append(compara_assinatura(as_a, textos))

