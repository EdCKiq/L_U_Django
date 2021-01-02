# Udemy_Django
## Irei colocar aqui tudo que estou aprendendo em Django com um curso na Udemy.

#### Criar um ambiente virtual:
> python3 -m venv --nome do ambiente virtual--

#### Para ativar:
> source --nome da venv--/bin/activate

#### No meu caso que também uso o Anaconda que inicia por padrão, antes de ativar a venv do Django desativar a venv do Anaconda:
> conda deactivate

#### E então instalar o django, ai vc sabe né **Pelo Amor de Deus**.

#### Para criar um arquivo que mostra o que foi usado e suas versões:
> pip freeze > nome do arquivo.txt

#### Para criar um Projeto Django:
> django-admin startproject --nome do projeto-- .
#### Para criar um App:
> django-admin startapp --nome do app--

#### Para criar um .gitignore:
> touch .gitignore
#### E dentro dele colocar o nome do arquivo que deve ser ignorado

#### Para rodar um servidor Django
> python3 manage.py runserver 

#### Para acrescentar um model a migrations
> python3 manage.py makemigrations

* Irá adicionar esse modelo de dados ao do Projeto além de criar um log de criação ou de modificação na pasta migrations.
#### Para fazer as migrações 
> python3 manage.py migrate
* Irá fazer toda a criação do sistema do BD

#### Para criar um super usúario para acessar o admin
> python3 manage.py createsuperuser

#### Arquivos estáticos em produção
> python3 manage.py collectstatic
* Cria uma pasta e redireciona todos os arquivos estáticos de todos os apps para a mesma que se localiza no root/Projeto
* A classificação dessa pasta e seu nome e feito nas configurações com a declaração lá informada

### Heroku 

* Para logar no Heroku e configurar o básico, basta seguir o Get Started no site após criar a conta, é tudo bem explicado.

* Para criar um app heroku
> heroku create nomeprojetodjango-iniciaisnome --buildpack heroku/python