
# APOD NASA PYTHON BOT
Autor: Lucas Henrique da Silva


### Explicando a lógica utilizada

A logica foi separar a utilizacao das API`s de forma que pudessemos isolar ao máximo a funcionalidade que cada API representaria.

Na API da NASA, implementamos funcoes que retornam as imagen conforme escolha do usuario na solicitação ao Bot.

Na API do Telegram, ficou alem da programacao da API em sim, algumas validacoes e regras de funcionamento.

Alem dessas APIs, fiz uso de um banco local para salvar chat_id dos usuários que gostariam de receber as fotos do dia, automaticamente em um horário pré-determinado.


### Dificuldades encontradas durante o desenvolvimento
Devido ao pouco tempo e pelo escopo genárico, o foco precisou ser intensificado para que as ideias ou novas funcoes nao viessem a comprometer a entrega principal

Outra ponto é que a API do telegram para python é deveras confusa pois a principal lib tem diversas versões, com inumeras mudanças e foi preciso ter um bom controle de versao das dependencias.

### Como interagir com o bot (lista de comandos, etc.)
Para interagir com o bot, basta seguir os passos abaixo:

1. Ao acessar o bot no telegram atraves [deste link](www.t.me/nasaApodPy_bot), o usuário inicia a interação com o bot, enviando o comando **/start**
2. A partir do comando incial, o bot irá sugerir as seguintes opções para o usuário.
* Foto do dia
* Foto de uma determinada data (nessa opção, será necessário fornecer a data)
* Foto dos últimos 5 dias (essa opção poderia ser customizada de várias formas)
* Solicitar envio automatico diariamente

3. Com base nessas solicitações, o bot irá realizar a ação conforme indicado.


### Link para o bot no Telegram para facilitar o teste.
www.t.me/nasaApodPy_bot 