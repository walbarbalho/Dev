Instalações em geral
-- Python: usar a opção personalizada e mandar instalar para todos os usuários e criar variáveis de ambiente
-- Rancher: desmarcar a opção do Kubernets

Iniciar o projeto Django

Criar ambiente virtual
```
# Para ver onde o Python está instalado
gcm python -Syntax ou gcm python
# Mostra qual Python está sendo utilizado
which pyhton
# Criar
python -m venv venv
.venv/scripts/activate
# Ativando e desativando meu ambiente virtual
# Windows:
.\venv\Scripts\activate
# Linux e Mac:
source venv/bin/activate
# Desativar:
deactivate
# PowerShell - se ocorrer algum problema ao habilitar o ambiente virtual
# Abrir o PowerShell como administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Para visualisar
Get-ExecutionPolicy -List
```
Git clone
```
$ git clone --recurse-submodules http://10.247.234.89/automacao/asa-1500/eb3.git
$ cd eb3/framework
$ git submodule foreach --recursive git checkout master
$ git submodule foreach --recursive git pull

# Após o clone instalar o poetry
pip install poetry==1.5.1
# Cria o amebiente virtual
poetry install
# Novo comando para gerar todas as tabelas do banco e já criar usuários
python manage.py init
```

Instalar e iniciar o django
```
pip install django
django-admin startproject project .
python manage.py startapp contact #contact é o nome do app - comando para criar app
```

Configurar o git
```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
# Para mandar as atualizações para o servidor remoto
git push
# Para buscar as alterações do servidor remoto
git pull
```

Arquivo Requiriments
```
# Lista no terminal os pacotes Python instalados no seu ambiente
pip freeze
# Gerar o arquivo
pip freeze > requirements.txt
# Para instalar os arquivos
pip install -r requirements.txt
```

Instalações à parte
```
# Rancher
https://github.com/rancher-sandbox/rancher-desktop/releases
# GetText Static
https://mlocati.github.io/articles/gettext-iconv-windows.html
```

Migrando a base de dados do Django
```
# Gerencia as mudanças na estrutura do banco de dados de uma aplicação
python manage.py migrate
# Analisa se foram feitas mudanças nos modelos
python manage.py makemigrations
# Para criar o menu
python -m aperam.crm.eb3.frontend.manage sitetree_resync_apps

# Para gerar os arquivos de tradução
python manage.py compilemessages

# Novo comando para gerar todas as tabelas do banco e já criar usuários
python manage.py init
```

Criando e modificando a senha de um super usuário Django - FrontEnd
```
python manage.py createsuperuser
python manage.py changepassword USERNAME
# Para rodar a aplicação
python manage.py runserver
```
Trabalhando com o model do Django

```python
# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
```


# Comando:
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
