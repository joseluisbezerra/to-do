# To-do
Aplicação web de um gerenciador de tarefas feito com o framework Django

# O que há no projeto
- Sistema de autenticação
- CRUD
- Dashboard simples das tarefas
- Filtros simples para as tarefas
- Templates resposivas e simples feitas com Bootstrap
- Paginação
- Mensagens


# Instalação
1. Crie um ambiente virtual:
```
python3 -m venv myvenv
```
2. Ative o ambiente virtual;
3. Instale as dependências:
```
(myvenv) pip install -r requirements.txt
```
4. Em seguida você vai precisar criar um arquivo .env:
```
(myvenv) python contrib/env_gen.py
```
5. Sincronize a base de dados:
```
(myvenv) python manage.py migrate
```
6. Crie um super usuário (Administrador do sistema):
```
(myvenv) python manage.py createsuperuser
```
7. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
```
(myvenv) python manage.py runserver
```