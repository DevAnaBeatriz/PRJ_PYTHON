import random


def escolher_palavra_por_tema(tema):
    # Temas para listas de palavras relacionadas
    temas = {
        1: ["banana", "laranja", "uva", "morango", "abacaxi"],
        2: ["vermelho", "azul", "verde", "amarelo", "roxo"],
        3: ["python", "java", "javascript", "csharp", "ruby"],
        4: ["colar", "pulseira", "anel", "chapeu", "oculos"],
        5: ["violao", "piano", "flauta", "trompete", "bateria"]
    }

    # Verificar se o tema é válido
    if tema not in temas:
        print("Tema inválido. Escolha um tema disponível.")
        return None

    # Escolher uma palavra aleatória do tema escolhido
    return random.choice(temas[tema])


def exibir_palavra_oculta(palavra, letras_adivinhadas):
    # Construir uma string que representa a palavra oculta, revelando letras adivinhadas
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta


def jogar_forca():
    print("Escolha um tema para a palavra:")
    print("1. Frutas")
    print("2. Cores")
    print("3. Linguagens de Programação")
    print("4. Acessórios")
    print("5. Instrumentos Musicais")

    while True:
        try:
            tema_escolhido = int(input("Digite o número correspondente ao tema: "))
            palavra = escolher_palavra_por_tema(tema_escolhido)

            # Se o tema for inválido, pedir ao usuário para escolher novamente
            if palavra is not None:
                break
        except ValueError:
            print("Entrada inválida. Digite um número correspondente ao tema.")

    letras_adivinhadas = []
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao jogo da forca!")
    print(exibir_palavra_oculta(palavra, letras_adivinhadas))

    while tentativas < tentativas_maximas:
        tentativa = input("\nDigite uma letra ou a palavra completa: ").lower()

        if len(tentativa) == 1 and tentativa.isalpha():
            if tentativa in letras_adivinhadas:
                print("Você já tentou essa letra. Tente novamente.")
            elif tentativa in palavra:
                letras_adivinhadas.append(tentativa)
                print("Letra correta!")
            else:
                tentativas += 1
                print(f"Letra incorreta! Você tem {tentativas_maximas - tentativas} tentativas restantes.")

            palavra_atual = exibir_palavra_oculta(palavra, letras_adivinhadas)
            print(palavra_atual)

            if palavra_atual == palavra:
                print("Parabéns! Você adivinhou a palavra.")
                break
        elif len(tentativa) > 1 and tentativa.isalpha():
            if tentativa == palavra:
                print("Parabéns! Você adivinhou a palavra.")
                break
            else:
                tentativas += 1
                print(f"Palavra incorreta! Você tem {tentativas_maximas - tentativas} tentativas restantes.")
        else:
            print("Entrada inválida. Digite apenas uma letra ou a palavra completa.")

    if tentativas == tentativas_maximas:
        print(f"\nFim de jogo. Você excedeu o número máximo de tentativas. A palavra era: {palavra}")


if __name__ == "__main__":
    jogar_forca()
