class TarefaView:
    def exibir_menu(self):
        print("\n--- Gerenciador de Tarefas (MVC) ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Excluir Tarefa")
        print("0. Sair")
        return input("Escolha uma opção: ")

    def exibir_tarefas(self, tarefas):
        print("\n--- Lista de Tarefas ---")
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        for t in tarefas:
            status = "[X]" if t.concluida else "[ ]"
            print(f"{t.id} - {status} {t.titulo}")

    def pedir_titulo_tarefa(self):
        return input("Digite o título da nova tarefa: ")

    def pedir_id_tarefa(self):
        try:
            return int(input("Digite o ID da tarefa para concluir: "))
        except ValueError:
            return -1

    def pedir_id_excluir(self):
        try:
            return int(input("Digite o ID da tarefa para EXCLUIR: "))
        except ValueError:
            return -1

    def exibir_mensagem(self, mensagem):
        print(f"\nAviso: {mensagem}")
