![](https://i.imgur.com/xG74tOh.png)

# 🚀 Desafio Técnico: APOD Telegram Bot

## 🌌 Visão Geral do Projeto:

Imagine poder começar o dia vendo a imensidão do espaço! Neste desafio, você utilizará suas habilidades em programação para trazer as estrelas mais perto de nós. Você criará um bot de Telegram que enviará a "Astronomy Picture of the Day" (APOD), fornecida pela API da NASA, diretamente em um chat no Telegram.

![](./github/example.gif)

## Requisitos do Projeto

Este projeto tem os seguintes requisitos:

- Integrar-se com a API da NASA para obter o APOD.
- Integrar-se com a API do Telegram para criar um bot.
- O bot é capaz de enviar a imagem do dia automaticamente para um chat no Telegram.
- Permite que o usuário solicite a imagem APOD de uma data específica enviando uma mensagem para o bot.

## Lógica Utilizada

O projeto foi desenvolvido em dart, a aplicação realiza uma requisição ao inicializar para configurar o webhook do telegram (para ser notificado sempre que um chat é atualizado). Durante o funcionamento da aplicação, há 1 rota ("host:8080/") que é acionada pelo telegram e dispara um evento para um service que, a depender do comando enviado, pode realizar uma requisição à API da NASA, para enviar a imagem para o chat, ou enviar outro tipo de mensagem (como um help, por exemplo).

# Principais dificuldades encontradas durante o desenvolvimento

- Aprender a usar a API da NASA.
- Aprender a usar a API do Telegram.
- Como Interagir com as APIs do telegram para enviar textos, imagens, etc.
- Utilizar o webhook ou polling para receber as atualizações do telegram. (prós e contras)
- Implementar a lógica para permitir que o usuário solicite a imagem APOD de uma data específica.

O bot pode ser acessado pelo seguinte link:

https://t.me/apod_bot

# Comandos

> /apod - Para obter a imagem do dia, basta enviar uma mensagem para o bot sem nenhum texto.

> /apod 2023-07-20 - Para obter a imagem APOD de uma data específica, envie uma mensagem para o bot com o formato /apod <data>, onde <data> é a data da imagem que deseja obter. Por exemplo, para obter a imagem APOD do dia 20 de julho de 2023, envie a seguinte mensagem:

> /help: Exibe uma lista de comandos disponíveis.

> /about: Exibe informações sobre o bot.

# Conclusão

Este projeto foi um desafio interessante e gratificante. Através dele, aprendi a usar a API da NASA e a API do Telegram para criar um bot que pode ser usado para obter imagens astronômicas.

O projeto está disponível no GitHub:

https://github.com/bard/apod_bot
