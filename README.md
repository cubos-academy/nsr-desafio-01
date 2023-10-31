# 🚀 Desafio Técnico: APOD Telegram Bot (resolução)

## 🤖 Link para acessar e testar!
https://t.me/italoa_apod_bot

## 🌌 Visão Geral do Projeto:
Imagine poder começar o dia vendo a imensidão do espaço! Neste desafio, você utilizará suas habilidades em programação para trazer as estrelas mais perto de nós. Você criará um bot de Telegram que enviará a "Astronomy Picture of the Day" (APOD), fornecida pela API da NASA, diretamente em um chat no Telegram.

## 🛠 Lógica e ferramentas utilizadas:
Nesse projeto, utilizei Python como linguagem de programação seguindo o paradigma de programação funcional + Flask (framework web). Para atender as mensagens recebidas de usuários pelo Bot, apontei meu app Flask como webhook  pedi para o Bot fazer uma request POST para ele em todos os momentos em que ele recebesse uma mensagem. Para deixar esse webhook acessível publicamente para os servers do Telegram conseguirem localiza-lo, utilizei o Render para deixar o webhook no ar.

## 📋 Passo a passo de como rodar:
Para rodar esse projeto localmente, você precisa:
1. Instalar as dependências listadas em requirements.txt;
2. Criar um arquivo .env e nele declarar 3 variáveis de ambiente, sendo elas:
  2.1. RENDER_API_TOKEN # Requerida para utilizar o Render;
  2.2. TELEGRAM_API_KEY # Requerida para utilizar a API do Telegram (https://core.telegram.org/bots/api);
  2.3. NASA_API_KEY # Requerida para utilizar as APIs da NASA (https://api.nasa.gov/).
3. Após declarar as variáveis, basta rodar o projeto utilizando 'flask --app src\app.py run'.
