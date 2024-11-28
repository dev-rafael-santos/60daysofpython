"""
Função pode_dirigir e verificação da entrada de idade do usuário.

"""
def pode_dirigir(idade):
    """
    Verifica se a pessoa pode dirigir com base na idade.
    
    Parâmetros:
    idade (int): A idade da pessoa.
    
    Retorna:
    bool: True se a idade for maior ou igual a 18, False caso contrário.
    """

    idade = int(idade)
    if idade >= 18:
        return True
    return False

try:
    input_user = int(input("Digite a sua idade: "))
    print(pode_dirigir(input_user))
except ValueError:
    print("Entrada invalida. Por favor, digite um numero inteiro.")
