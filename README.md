# Evetex

sistema de Eventos encomendado pela Morena

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com python 3.6
3. Ative p virtualenv
4. Instale as dependências
5. Configure a instância com .env
6. Execute os testes

``` console
git clone git@github.com:belaeifert/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

```


## Como Fazer o Deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina o DEBUG=False
4. Configure o serviço de email
6. Envie o código para o Heroku

``` console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY = python contrib/secret_gen.py
heroki config:set DEBUG=False
#configura o email
git push heroku master --force

```