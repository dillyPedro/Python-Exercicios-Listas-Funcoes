'''
Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos  que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.
'''

def calcular_pontos(lista1, lista2):
    pontos = 0
    for gol_marcado, gol_sofrido in zip(lista1, lista2):
        if(gol_marcado > gol_sofrido):
            pontos += 3
        elif(gol_marcado == gol_sofrido):
            pontos += 1
        else:
            pontos += 0
    max_pontos = 3 * len(lista1)
    aproveitamento = pontos / max_pontos
    return pontos, aproveitamento

gols_marcados = [3, 2, 5, 1, 0, 4, 3, 2, 2, 1]

gols_sofridos = [1, 2, 3, 2, 1, 2, 3, 1, 3, 1]

total_pontos, total_aproveitamento = calcular_pontos(gols_marcados, gols_sofridos)

print(f'Total de Pontos = {total_pontos} | Aproveitamento = {100 * total_aproveitamento:.2f}%.')