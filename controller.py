from model import TarefaModel
from view import TarefaView

class TarefaController:
    def __init__(self):
        self.model = TarefaModel()
        self.view = TarefaView()

    def iniciar(self):
        while True:
            opcao = self.view.exibir_menu()

            if opcao == '1':
                titulo = self.view.pedir_titulo_tarefa()
                if titulo.strip():
                    self.model.adicionar_tarefa(titulo)
                    self.view.exibir_mensagem("Tarefa adicionada com sucesso!")
                else:
                    self.view.exibir_mensagem("O título não pode ser vazio.")

            elif opcao == '2':
                tarefas = self.model.listar_tarefas()
                self.view.exibir_tarefas(tarefas)

            elif opcao == '3':
                id_tarefa = self.view.pedir_id_tarefa()
                sucesso = self.model.concluir_tarefa(id_tarefa)
                if sucesso:
                    self.view.exibir_mensagem("Tarefa marcada como concluída!")
                else:
                    self.view.exibir_mensagem("Tarefa não encontrada ou ID inválido.")
            
            elif opcao == '4':
                id_tarefa = self.view.pedir_id_excluir()
                sucesso = self.model.excluir_tarefa(id_tarefa)
                if sucesso:
                    self.view.exibir_mensagem("Tarefa excluída com sucesso!")
                else:
                    self.view.exibir_mensagem("Tarefa não encontrada ou ID inválido.")

            elif opcao == '0':
                self.view.exibir_mensagem("Saindo do sistema...")
                break

            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.")
