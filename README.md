# to-do
Aplicação web de um gerenciador de tarefas feito em Django

# Dependências
- python - Versão 3.5+
- Django==2.1.5
- django-crispy-forms==1.7.2

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
4. Sincronize a base de dados:
```
(myvenv) python manage.py migrate
```
5. Crie um usuário (Administrador do sistema):
```
(myvenv) python manage.py createsuperuser
```
6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
```
(myvenv) python manage.py runserver
```
