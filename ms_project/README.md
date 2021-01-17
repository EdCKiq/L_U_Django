### Django com MySQL
* Talves seja necessário rodar o código abaixo para instalar certas dependências
> sudo apt install libmysqlclient-dev python3-dev 

> pip3 install MySQL

* Para rodar códigos no terminal do heroku
> heroku run comandodesejado

* Resetar BD do Heroku
> heroku pg:reset DATABASE_URL
* Após é necessário recriar as tabelas com
> heroku run python3 manage.py makemigrations
> heroku run python3 manage.py migrate
* e recriar um super usuário
> heroku run python3 manage.py createsuperuser