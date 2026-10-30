import sqlite3

class Tarefa:
    def __init__(self, id_tarefa, titulo, concluida=False):
        self.id = id_tarefa
        self.titulo = titulo
        self.concluida = concluida

class TarefaModel:
    def __init__(self):
        self.db_name = 'tarefas.db'
        self._criar_tabela()

    def _criar_tabela(self):
        """Cria o arquivo e a tabela se não existirem."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    concluida INTEGER NOT NULL DEFAULT 0
                )
            ''')
            conn.commit()

    def adicionar_tarefa(self, titulo):
        """Insere uma nova tarefa no banco de dados."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tarefas (titulo, concluida) VALUES (?, 0)', (titulo,))
            conn.commit()
            return Tarefa(cursor.lastrowid, titulo)

    def listar_tarefas(self):
        """Busca todas as tarefas e as converte em objetos Tarefa."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, titulo, concluida FROM tarefas')
            linhas = cursor.fetchall()
            
            tarefas = []
            for linha in linhas:
                tarefas.append(Tarefa(linha[0], linha[1], bool(linha[2])))
            return tarefas

    def concluir_tarefa(self, id_tarefa):
        """Atualiza o status da tarefa para concluída (1)."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?', (id_tarefa,))
            conn.commit()
            return cursor.rowcount > 0

    def excluir_tarefa(self, id_tarefa):
        """Remove a tarefa do banco de dados pelo ID."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_tarefa,))
            conn.commit()
            return cursor.rowcount > 0
