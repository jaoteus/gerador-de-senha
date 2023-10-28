'''
Password generator.
Gerador de senha.
Criado por João Mateus em 28/10/2023
Made by João Mateus in 10/28/2023
'''
import random

algarismos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&']

# numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# simbolos = ['!', '@', '#', '$', '%', '&']
senha_gerada = []
entrada_quantidade_de_algarismos = 0

def gerar_senha_aleatoria(entrada_quantidade_de_algarismos):
    global algarismo_aleatorio
    while len(senha_gerada) < entrada_quantidade_de_algarismos:
        algarismo_aleatorio = random.choice(algarismos)
        senha_gerada.append(algarismo_aleatorio)
try:
    entrada_quantidade_de_algarismos = int(input("Digite a quantidade de algarismo que você deseja para a sua senha: "))
    if entrada_quantidade_de_algarismos < 18:
        print("Não podemor gerar uma senha muito curta, você pode pôr em risco a segurança da sua conta!")
    else:
        gerar_senha_aleatoria(entrada_quantidade_de_algarismos)
except ValueError:
    print("Digite apenas números")
