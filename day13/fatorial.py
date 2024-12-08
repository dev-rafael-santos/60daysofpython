# pylint: disable=consider-using-in
"""
o que eh um fatorial
fatorial eh um calculo em matematica onde multiplicamos os valores a partir do numero passado
5! = 5 x 4 x 3 x 2 x 1 = 120
3! = 3 x 2 x 1 = 6
"""
def fatorial(numero):
    """
    Calcula o fatorial de um número usando recursão.

    :param n: Número inteiro não negativo.
    :return: Fatorial de n.
    """
    if numero < 0:
        raise ValueError("O numero deve ser positivo")

    #entao essa condicional retorna 1 se caso o numero da funcao for 0 ou 1
    if numero == 0 or numero == 1:
        return 1

    #recursividade
    return numero * fatorial(numero - 1)

# print(fatorial(-1))

try:
    print(f"Fatorial igual a {fatorial(-1)}")
except ValueError as e:
    print(e)
