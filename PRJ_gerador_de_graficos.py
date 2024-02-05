import matplotlib.pyplot as plt

# Função para validar e obter uma lista de valores numéricos do usuário
def obter_dados_numericos():
    while True:
        try:
            entrada_usuario = input("Digite uma lista de valores numéricos separados por espaços: ")
            dados_numericos = [float(valor) for valor in entrada_usuario.split()]
            return dados_numericos
        except ValueError:
            print("Entrada inválida. Insira valores numéricos válidos.")

# Função para gerar gráfico de barras
def gerar_grafico_barras(dados_numericos):
    plt.bar(range(len(dados_numericos)), dados_numericos)
    plt.xlabel("Índice do Dado")
    plt.ylabel("Valor")
    plt.title("Gráfico de Barras")
    plt.show()

# Função para gerar gráfico de pizza
def gerar_grafico_pizza(dados_numericos):
    plt.pie(dados_numericos, labels=[f"Dado {i+1}" for i in range(len(dados_numericos))], autopct='%1.1f%%', startangle=140)
    plt.title("Gráfico de Pizza")
    plt.show()

# Função principal
def main():
    # Solicitar ao usuário que insira dados numéricos
    dados_numericos = obter_dados_numericos()

    # Verificar se há dados suficientes para gerar gráficos
    if len(dados_numericos) == 0:
        print("Nenhum dado fornecido. Encerrando o programa.")
        return

    # Solicitar ao usuário que escolha o tipo de gráfico
    while True:
        try:
            escolha_grafico = input("Escolha o tipo de gráfico (1 - Barras, 2 - Pizza): ")
            escolha_grafico = int(escolha_grafico)

            # Validar a escolha do usuário
            if escolha_grafico in [1, 2]:
                break
            else:
                print("Escolha inválida. Por favor, digite 1 para Gráfico de Barras ou 2 para Gráfico de Pizza.")
        except ValueError:
            print("Entrada inválida. Insira um número.")

    # Gerar o gráfico selecionado
    if escolha_grafico == 1:
        gerar_grafico_barras(dados_numericos)
    else:
        gerar_grafico_pizza(dados_numericos)

if __name__ == "__main__":
    main()
