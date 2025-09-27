# API-v1
Criação de API Atividade de Sistemas Corporativos

# Comandos Utilizados
py -3 -m venv .venv
.venv\Scripts\activate
pip install django djangorestframework
django-admin startproject BackEnd .
django-admin startapp Banco 
pip install mssql-django 
python manage.py inspectdb > banco/models.py (Esse comando inspeciona o db e cria os models de acordo com o banco criado)

