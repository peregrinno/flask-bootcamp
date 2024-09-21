import requests
import os

# Teste 1: Valida retorno de mensagem simples
def test1(BASE_URL):
    try:
        response = requests.get(f'{BASE_URL}/test1')
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        expected_data = {'message': 'Olá mundo!'}
        assert response.json() == expected_data, f"Expected {expected_data}, got {response.json()}"
        print("Teste 1 passou com sucesso!")
    except AssertionError as e:
        print(f"Erro no Teste 1: {e}")

# Teste 2: Soma de dois números
def test2(BASE_URL):
    try:
        num1, num2 = 3, 5
        payload = {'num1': num1, 'num2': num2}
        response = requests.post(f'{BASE_URL}/test2', json=payload)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        expected_data = {'message': str(num1 + num2)}
        assert response.json() == expected_data, f"Expected {expected_data}, got {response.json()}"
        print("Teste 2 passou com sucesso!")
    except AssertionError as e:
        print(f"Erro no Teste 2: {e}")

# Teste 3: Ordenação de lista de números
def test3(BASE_URL):
    try:
        numbers = [7, 1, 5, 9, 3, 2, 8, 6, 4, 0]
        payload = {'numbers': numbers}
        response = requests.post(f'{BASE_URL}/test3', json=payload)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        expected_data = {'message': str(sorted(numbers))}
        assert response.json() == expected_data, f"Expected {expected_data}, got {response.json()}"
        print("Teste 3 passou com sucesso!")
    except AssertionError as e:
        print(f"Erro no Teste 3: {e}")

# Teste 4: Troca de nome e telefone
def test4(BASE_URL):
    try:
        payload = {'nome': '12345', 'telefone': 'João'}
        response = requests.post(f'{BASE_URL}/test4', json=payload)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        expected_data = {'nome': 'João', 'telefone': '12345'}
        assert response.json() == expected_data, f"Expected {expected_data}, got {response.json()}"
        print("Teste 4 passou com sucesso!")
    except AssertionError as e:
        print(f"Erro no Teste 4: {e}")

# Teste 5: Retorno de nome e telefone aleatório
def test5(BASE_URL):
    try:
        payload = [
            {'nome': 'João', 'telefone': '12345'},
            {'nome': 'Maria', 'telefone': '67890'},
            {'nome': 'José', 'telefone': '11223'},
            {'nome': 'Ana', 'telefone': '44556'},
            {'nome': 'Paulo', 'telefone': '77889'}
        ]
        response = requests.post(f'{BASE_URL}/test5', json=payload)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        data = response.json()
        assert data in payload, f"Expected one of {payload}, got {data}"
        print("Teste 5 passou com sucesso!")
    except AssertionError as e:
        print(f"Erro no Teste 5: {e}")

# Teste 6: Exclusão de item com id específico
def test6(BASE_URL):
    try:
        id_to_exclude = 3
        payload = [
            {'id': 1, 'nome': 'João', 'telefone': '12345'},
            {'id': 2, 'nome': 'Maria', 'telefone': '67890'},
            {'id': 3, 'nome': 'José', 'telefone': '11223'},
            {'id': 4, 'nome': 'Ana', 'telefone': '44556'},
            {'id': 5, 'nome': 'Paulo', 'telefone': '77889'}
        ]
        response = requests.post(f'{BASE_URL}/test6?id={id_to_exclude}', json=payload)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        expected_data = [item for item in payload if item['id'] != id_to_exclude]
        assert response.json() == expected_data, f"Expected {expected_data}, got {response.json()}"
        print("Teste 6 passou com sucesso!")
    except AssertionError as e:
        print(f"Erro no Teste 6: {e}")