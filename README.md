# Projeto
Projeto desenvolvido com o intuito de criar um bot para telegram. 
O bot utiliza flask e armazena as informações dos usuários e as 
mensagens enviadas em um banco de dados relacional.

## Como Funciona?

Basta colocar o token do seu bot no arquivo *application/bot/utils.py*. 
Feito isso, você conseguirá conversar com seu bot a partir do telegram.

## Rodando o projeto


Caso queira o projeto rodando localmente é preciso usar um serviço 
de SSH tunneling, eu utilizei o [localhost.run](https://localhost.run/) 
em meus testes. Você pode utilizar o programa da seguinte forma:

```bash
$ ssh -R 80:localhost:5000 ssh.localhost.run
```

Assim que o comando é executado e você aceita fazer a conexão 
ssh, aparecerá um link com o qual é preciso criar um webhook 
para seu bot funcionar localmente. Para isso:

```bash
$ curl -X GET \
https://api.telegram.org/bot<token_do_seu_bot>/setWebhook?url=<url_gerada>
```

**OBS:** A url que inserida no comando anterior deve começar com https e **não** com http

Após as etapas anteriores, basta instalar os requirements:

```bash
$ python -m pip install -r requirements.txt
```
E rodar o projeto com:

```bash
$ python app.py
```

Para funcionar corretamente, o servidor flask e a conexão ssh devem estar 
rodando ao mesmo tempo em terminais diferentes.
