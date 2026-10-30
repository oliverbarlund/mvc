# Gerenciador de Tarefas (MVC)

Este projeto é um Gerenciador de Tarefas desenvolvido em Python com banco de dados SQLite, implementando rigorosamente o padrão de arquitetura **MVC (Model-View-Controller)**.

## Estrutura do Projeto
- `model.py`: Gerencia os dados, as regras de negócio e a comunicação com o SQLite.
- `view.py`: Responsável exclusivamente pela interface com o usuário (inputs e prints no terminal).
- `controller.py`: Atua como intermediário, recebendo as ações da View e manipulando o Model.
- `main.py`: Ponto de entrada que inicializa a aplicação.

## Como rodar o projeto
1. Certifique-se de ter o Python instalado na sua máquina.
2. Abra o terminal ou prompt de comando nesta pasta.
3. Execute o comando: `python main.py`
