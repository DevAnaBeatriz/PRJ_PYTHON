import random


# Função para simular o lançamento de dados
def simular_lancamento_de_dados(num_dados, num_lancamentos):
    resultados = []

    for _ in range(num_lancamentos):
        # Simular o lançamento de cada dado
        resultado_lancamento = [random.randint(1, 6) for _ in range(num_dados)]
        resultados.append(resultado_lancamento)

    return resultados


# Função principal
def main():
    # Solicitar ao usuário o número de dados e o número de lançamentos
    while True:
        try:
            num_dados = int(input("Digite o número de dados a serem lançados: "))
            num_lancamentos = int(input("Digite o número de lançamentos desejados: "))

            # Validar entradas
            if num_dados > 0 and num_lancamentos > 0:
                break
            else:
                print("Por favor, insira valores positivos para o número de dados e lançamentos.")
        except ValueError:
            print("Entrada inválida. Insira um número inteiro válido.")

    # Simular o lançamento de dados
    resultados = simular_lancamento_de_dados(num_dados, num_lancamentos)

    # Exibir os resultados
    print("\nResultados dos lançamentos:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Lançamento {i}: {resultado}")


if __name__ == "__main__":
    main()
