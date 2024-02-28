import string

def caracteres_mais_frequentes(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.readline()

    #contagem de ocorrencias de cada caractere
    contagem_caracteres = {}
    for char in texto:
        if char.strip():
            if char in contagem_caracteres:
                contagem_caracteres[char] += 1
            else:
                contagem_caracteres[char] = 1

    #encontrar os caracteres mais frequentes
    max_ocorrencias = max(contagem_caracteres.values())
    caracteres_mais_frequentes = [char for char, ocorrencias in contagem_caracteres.items() if ocorrencias == max_ocorrencias]

    return caracteres_mais_frequentes, max_ocorrencias

nome_arquivo = "lista_gerada4.txt"
caracteres, quantidade = caracteres_mais_frequentes(nome_arquivo)
print("Caracteres mais frequentes:", caracteres)
print("Quantidade de ocorrências:", quantidade)

