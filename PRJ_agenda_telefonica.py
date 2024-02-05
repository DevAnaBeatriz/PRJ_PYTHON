# Classe para representar um contato na agenda
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

# Função para adicionar um novo contato à agenda
def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")

    # Criar uma nova instância de Contato
    novo_contato = Contato(nome, telefone)

    # Adicionar o contato à agenda
    agenda.append(novo_contato)
    print("Contato adicionado com sucesso!")

# Função para remover um contato da agenda
def remover_contato(agenda):
    if not agenda:
        print("Agenda vazia. Não há contatos para remover.")
        return

    # Exibir lista de contatos
    print("Contatos na agenda:")
    for i, contato in enumerate(agenda, start=1):
        print(f"{i}. {contato.nome} - {contato.telefone}")

    try:
        indice = int(input("Digite o número do contato que deseja remover: ")) - 1

        # Verificar se o índice é válido
        if 0 <= indice < len(agenda):
            contato_removido = agenda.pop(indice)
            print(f"Contato '{contato_removido.nome}' removido com sucesso!")
        else:
            print("Índice inválido. Por favor, escolha um número válido.")
    except ValueError:
        print("Entrada inválida. Insira um número.")

# Função para pesquisar um contato na agenda
def pesquisar_contato(agenda):
    if not agenda:
        print("Agenda vazia. Não há contatos para pesquisar.")
        return

    termo_pesquisa = input("Digite o nome do contato que deseja pesquisar: ")
    termo_pesquisa = termo_pesquisa.lower()

    # Filtrar contatos que contenham o termo de pesquisa no nome
    contatos_encontrados = [contato for contato in agenda if termo_pesquisa in contato.nome.lower()]

    if contatos_encontrados:
        print("\nContatos encontrados:")
        for i, contato in enumerate(contatos_encontrados, start=1):
            print(f"{i}. {contato.nome} - {contato.telefone}")
    else:
        print("Nenhum contato encontrado.")

# Função principal
def main():
    # Lista para armazenar os contatos
    agenda = []

    while True:
        print("\nOpções:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            adicionar_contato(agenda)
        elif escolha == '2':
            remover_contato(agenda)
        elif escolha == '3':
            pesquisar_contato(agenda)
        elif escolha == '4':
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
