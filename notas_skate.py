'''
Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

"Nota da manobra: [media]"
'''

def retornando_notas():
    contagem = 0
    for notas in range(0, 5):
        nota = float(input('Digite sua nota: '))
        lista_notas.append(nota)

def removendo_notas():
    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    lista_notas.remove(maior_nota)
    lista_notas.remove(menor_nota)

def media_notas():
    soma = 0
    for notas in lista_notas:
        soma = soma + notas
    media = soma / len(lista_notas)
    return media

lista_notas = []

# Chamando as funções:
retornando_notas()
removendo_notas()
media = media_notas()

print(f'Nota de Manobra = {media}')