'''
Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

O texto exibido ao fim deve ser parecido com:

"Nome completo: Ana Silva"

Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.
'''

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

# Criando um dicionário:
lista_atualizada = dict(zip(nomes, sobrenomes))
print(lista_atualizada)

# Transformando o dicionário "lista_atualizada" em uma lista:
nova_lista = [f'{chave} {valor}' for chave, valor in lista_atualizada.items()]
print(nova_lista)

# Utilizando o map():
lista_final = map(lambda lista: lista.title(), nova_lista)
lista_final = list(lista_final)
print(lista_final)

def imprimir_nomes():
    for nomes in lista_final:
        print(f'Nome Completo: {nomes}')

# Retornando a função:
imprimir_nomes()