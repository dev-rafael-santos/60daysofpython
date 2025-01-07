import json
from typing import Any

def salvar_dados(arquivo:str, dados: Any) -> None:
    """
    Salva os dados fornecidos em um arquivo json 
    
    :param arquivo: Caminho para o arquivo JSON
    :param dados: Os dados que serao armazenados no arquivo
        
    """
    
    with open(arquivo, 'w', encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        
        
def carregar_dados(arquivo:str) -> Any:
    """
    Le os dados do arquivo JSON    
    :param str: Caminho para o arquivo 
    return: Dados carregador  e lidos do arquivo JSON
    """
    try:
        with open (arquivo,'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("O arquivo nao foi encontrado, caminho do arquivo{arquivo}")
        return {}

dados_exemplos = {"nome": "Rafael", "cidade": "SP", "cargo":"programador" }

nome_arquivo = "nome_rafael.json"

salvar_dados(nome_arquivo, dados_exemplos)

dados_carregados = carregar_dados(nome_arquivo)

print ("Dados carregados:", dados_carregados)


