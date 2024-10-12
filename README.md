# Offline Task Manager

Um gerenciador de tarefas simples, desenvolvido com Django, que permite adicionar, editar e excluir tarefas offline.

## Principais Funcionalidades

- **Adicionar Tarefas**: Crie novas tarefas com nome e tempo estimado.
- **Listar Tarefas**: Visualize todas as tarefas em uma tabela.
- **Editar Tarefas**: Atualize tarefas existentes.
- **Excluir Tarefas**: Remova tarefas que não são mais necessárias.

## Como Configurar e Iniciar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu_usuario/offline_task_manager.git
   cd offline_task_manager
   ```

2. **Crie e ative um ambiente virtual**:

   ```bash
   python -m venv env
   source env/bin/activate  # No Windows use: env\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:

   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor**:

   ```bash
   python manage.py runserver
   ```

6. **Acesse o aplicativo**:

   Abra seu navegador e vá para `http://127.0.0.1:8000/tasks/`.
