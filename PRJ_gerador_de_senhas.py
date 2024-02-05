import random
import string


# Função para gerar senhas aleatórias e seguras
def gerar_senha(comprimento=12, usar_maiusculas=True, usar_numeros=True, usar_especiais=True):
    # Define os caracteres básicos como minúsculas
    caracteres = string.ascii_lowercase

    # Adiciona letras maiúsculas se a opção estiver habilitada
    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    # Adiciona números se a opção estiver habilitada
    if usar_numeros:
        caracteres += string.digits

    # Adiciona caracteres especiais se a opção estiver habilitada
    if usar_especiais:
        caracteres += string.punctuation

    # Gera a senha usando a função random.choice para cada caractere
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


# Função para obter o comprimento da senha, garantindo um valor mínimo de 8
def obter_comprimento_senha():
    while True:
        comprimento = int(input("Digite o comprimento da senha desejada (mínimo 8): "))
        if comprimento >= 8:
            return comprimento
        else:
            print("Comprimento inválido. A senha deve ter pelo menos 8 caracteres.")


# Função para obter a preferência do usuário, garantindo uma resposta válida
def obter_preferencia_usuario(mensagem):
    while True:
        resposta = input(mensagem).lower()
        if resposta == 's' or resposta == 'n':
            return resposta
        else:
            print("Resposta inválida. Por favor, digite 's' para Sim ou 'n' para Não.")


if __name__ == "__main__":
    # Solicita ao usuário o comprimento desejado da senha (mínimo 8)
    comprimento_senha = obter_comprimento_senha()

    usar_maiusculas = obter_preferencia_usuario("Incluir letras maiúsculas? (s/n): ") == 's'
    usar_numeros = obter_preferencia_usuario("Incluir números? (s/n): ") == 's'
    usar_especiais = obter_preferencia_usuario("Incluir caracteres especiais? (s/n): ") == 's'

    # Gera a senha com base nas preferências do usuário
    senha_gerada = gerar_senha(comprimento_senha, usar_maiusculas, usar_numeros, usar_especiais)

    # Exibe a senha gerada
    print(f'\nSenha gerada: {senha_gerada}')
