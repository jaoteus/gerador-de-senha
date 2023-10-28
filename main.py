'''
Password generator.
Gerador de senha.
Criado por João Mateus em 28/10/2023
Made by João Mateus in 10/28/2023
'''
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

simbolos = ['!', '@', '#', '$', '%', '&']


senha_gerada = ''
entrada_quantidade_de_algarismos = 0

def gerar_senha_aleatoria(entrada_quantidade_de_algarismos):
    global senha_gerada
    while len(senha_gerada) < entrada_quantidade_de_algarismos:
        '''
        1 - Alfabeto
        2 - Número
        3 - Símbolo    
        '''
        qual_o_proximo = random.randrange(1, 4)
        if qual_o_proximo == 1:
            algarismo_aleatorio = random.choice(letras)
            senha_gerada = senha_gerada + algarismo_aleatorio
        elif qual_o_proximo == 2:
            algarismo_aleatorio = random.choice(numeros)
            senha_gerada = senha_gerada + algarismo_aleatorio
        elif qual_o_proximo == 3:
            algarismo_aleatorio = random.choice(simbolos)
            senha_gerada = senha_gerada + algarismo_aleatorio
try:
    entrada_quantidade_de_algarismos = int(input("Digite a quantidade de algarismo que você deseja para a sua senha: "))
    if entrada_quantidade_de_algarismos < 18:
        print("Não podemor gerar uma senha muito curta, você pode pôr em risco a segurança da sua conta!")
    else:
        gerar_senha_aleatoria(entrada_quantidade_de_algarismos)
except ValueError:
    print("Digite apenas números")

# Output / Saída de dados
print(f"A senha gerada foi: {senha_gerada}")