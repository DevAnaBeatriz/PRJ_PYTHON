# Bem-vindo ao programa de conversão de unidades!
print("Olá! Este programa realiza diversas conversões de unidades de medida.")

# Função para converter quilômetros para milhas
def km_para_milhas(km):
    return km * 0.621371

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter quilos para libras
def quilos_para_libras(quilos):
    return quilos * 2.20462

# Função principal que contém a lógica principal do programa
def main():
    while True:  # Loop para continuar solicitando uma opção válida
        # Menu de opções para o usuário
        print("\nEscolha a conversão que deseja realizar:")
        print("1 - Quilômetros para Milhas")
        print("2 - Celsius para Fahrenheit")
        print("3 - Quilos para Libras")

        # Solicita ao usuário que escolha uma opção
        opcao = input("Digite o número da opção desejada (ou 's' para sair): ")

        # Verifica se o usuário deseja sair
        if opcao.lower() == 's':
            print("Até logo!")
            break

        # Verifica se a opção é um número
        if not opcao.isdigit():
            print("Por favor, insira apenas números.")
            continue  # Volta ao início do loop

        # Converte a opção para inteiro
        opcao = int(opcao)

        # Verifica a opção escolhida e realiza a conversão
        if opcao == 1:
            # Solicita a entrada do usuário para a quantidade em quilômetros
            km = input("Digite a quantidade em quilômetros: ")
            # Verifica se a entrada é um número
            if not km.replace('.', '', 1).isdigit():
                print("Por favor, insira apenas números para a quantidade.")
                continue  # Volta ao início do loop
            km = float(km)
            # Chama a função e imprime o resultado
            print(f"{km} quilômetros é igual a {km_para_milhas(km):.2f} milhas.")
        elif opcao == 2:
            # Solicita a entrada do usuário para a temperatura em Celsius
            celsius = input("Digite a temperatura em Celsius: ")
            # Verifica se a entrada é um número
            if not celsius.replace('.', '', 1).isdigit():
                print("Por favor, insira apenas números para a temperatura.")
                continue  # Volta ao início do loop
            celsius = float(celsius)
            # Chama a função e imprime o resultado
            print(f"{celsius} graus Celsius é igual a {celsius_para_fahrenheit(celsius):.2f} graus Fahrenheit.")
        elif opcao == 3:
            # Solicita a entrada do usuário para o peso em quilos
            quilos = input("Digite o peso em quilos: ")
            # Verifica se a entrada é um número
            if not quilos.replace('.', '', 1).isdigit():
                print("Por favor, insira apenas números para o peso.")
                continue  # Volta ao início do loop
            quilos = float(quilos)
            # Chama a função e imprime o resultado
            print(f"{quilos} quilos é igual a {quilos_para_libras(quilos):.2f} libras.")
        else:
            # Se a opção digitada não estiver entre as opções válidas
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chamada da função main para iniciar o programa
if __name__ == "__main__":
    main()
