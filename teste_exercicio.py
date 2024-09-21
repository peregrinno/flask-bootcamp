"""
Exercicio de criação de rotas com flask, automatizado.

Bom,  a atividade é muito simples, nesse arquivo terá 10 testes de rota 
nos quais são testado automaticamente a entrada e saida do seu servidor Flask.

A sua missão é fazer com que todas os testes funcionem ao final da execução.

-------------------- INSTRUÇÔES --------------------

1. Inicie o servidor flask que pode estar nesse projeto ou em outro de sua preferência.
2. Com o servidor iniciado, execute esse arquivo com o seu terminal de preferência.
3. Ao final de cada execução, lembre de fechar o terminal do teste e abrir outro para testar novamente.

BOA SORTE!!!

"""

import os
import requests
from testes import testes as ts

BASE_URL = 'http://127.0.0.1:5000'

print("TESTE AUTOMATIZADO DE API - FLASK")

def check_server():
    try:
        response = requests.get(BASE_URL)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def run_tests():
    if not check_server():
        print(f"Servidor não está rodando na URL {BASE_URL}. Por favor, verifique se a API está em execução.")
        os.system("pause")
        return

    ts.test1(BASE_URL)
    ts.test2(BASE_URL)
    ts.test3(BASE_URL)
    ts.test4(BASE_URL)
    ts.test5(BASE_URL)
    ts.test6(BASE_URL)
    print("Todos os testes passaram com sucesso!")
    os.system("pause")
    
run_tests()
