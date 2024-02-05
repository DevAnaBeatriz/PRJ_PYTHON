# Classe para representar uma tarefa
class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa(lista_tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa (baixa, média, alta): ")

    # Criar uma nova instância de Tarefa
    nova_tarefa = Tarefa(descricao, prioridade)

    # Adicionar a tarefa à lista
    lista_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para remover uma tarefa da lista
def remover_tarefa(lista_tarefas):
    if not lista_tarefas:
        print("Lista de tarefas vazia. Não há tarefas para remover.")
        return

    print("Tarefas:")
    for i, tarefa in enumerate(lista_tarefas):
        print(f"{i + 1}. {tarefa.descricao} - Prioridade: {tarefa.prioridade}")

    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1

        # Verificar se o índice é válido
        if 0 <= indice < len(lista_tarefas):
            tarefa_removida = lista_tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida.descricao}' removida com sucesso!")
        else:
            print("Índice inválido. Por favor, escolha um número válido.")
    except ValueError:
        print("Entrada inválida. Insira um número.")

# Função para visualizar todas as tarefas pendentes
def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Lista de tarefas vazia. Não há tarefas para exibir.")
        return

    print("Tarefas pendentes:")
    for i, tarefa in enumerate(lista_tarefas):
        print(f"{i + 1}. {tarefa.descricao} - Prioridade: {tarefa.prioridade}")

# Função principal
def main():
    # Lista para armazenar as tarefas
    tarefas = []

    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Visualizar Tarefas Pendentes")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            remover_tarefa(tarefas)
        elif escolha == '3':
            visualizar_tarefas(tarefas)
        elif escolha == '4':
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
