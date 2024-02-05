# Função para contar o número de palavras em um texto
def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

# Função para contar o número de caracteres em um texto (incluindo espaços)
def contar_caracteres(texto):
    return len(texto)

# Função para calcular a frequência de cada palavra em um texto
def calcular_frequencia_palavras(texto):
    palavras = texto.split()
    frequencia = {}

    for palavra in palavras:
        # Remover pontuações simples (.,;:?!)
        palavra = palavra.strip(".,;:?!").lower()
        # Incrementar a contagem da palavra no dicionário de frequência
        frequencia[palavra] = frequencia.get(palavra, 0) + 1

    return frequencia

# Função principal
def main():
    # Receber o texto do usuário
    texto_usuario = input("Digite o texto que você deseja analisar:\n")

    # Calcular o número de palavras
    num_palavras = contar_palavras(texto_usuario)
    print(f"Número de palavras: {num_palavras}")

    # Calcular o número de caracteres
    num_caracteres = contar_caracteres(texto_usuario)
    print(f"Número de caracteres (incluindo espaços): {num_caracteres}")

    # Calcular a frequência de palavras
    frequencia_palavras = calcular_frequencia_palavras(texto_usuario)

    # Exibir a frequência de palavras
    print("\nFrequência de palavras:")
    for palavra, frequencia in frequencia_palavras.items():
        print(f"{palavra}: {frequencia}")

if __name__ == "__main__":
    main()
