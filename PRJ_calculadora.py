def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

# Função para exibir o menu
def mostrar_menu():
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

# Loop principal
while True:
    # Mostrar o menu e obter a escolha do usuário
    mostrar_menu()
    escolha = input("Digite o número da operação desejada (1/2/3/4/5): ")

    # Verificar se a escolha é válida
    if escolha not in ['1', '2', '3', '4', '5']:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

    # Verificar se o usuário escolheu sair
    if escolha == '5':
        print("Calculadora encerrada.")
        break

    try:
        # Obter os números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        # Tratar exceção se os números inseridos não forem válidos
        print("Erro: Por favor, insira números válidos.")
        continue

    # Realizar a operação escolhida e imprimir o resultado
    if escolha == '1':
        print(num1, "+", num2, "=", adicao(num1, num2))
    elif escolha == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))
    elif escolha == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))
    elif escolha == '4':
        resultado_divisao = divisao(num1, num2)
        print(num1, "/", num2, "=", resultado_divisao)

if __name__ == "__main__":
    mostrar_menu()