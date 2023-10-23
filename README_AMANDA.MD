![](https://www.nasa.gov/wp-content/uploads/2021/05/nasa-logo-web-rgb.png)

# NASA Bot para Telegram

Este é um projeto Python que cria um bot para o Telegram que interage com a API da NASA para fornecer a "Foto do Dia" (Astronomy Picture of the Day - APOD) e informações relacionadas.
Desafio criado pela Cubos Academy.

## Autora

**Amanda Karolline Barbosa Sousa** - [amandakarolline](https://github.com/amandakarolline)
<br><a href = "mailto:amandakarolline@hotmail.com"><img src="https://img.shields.io/badge/-Hotmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a></br>

## Link do bot

O bot está disponível no Telegram através do link: [Desafio Bot - Amanda](https://web.telegram.org/k/#@Desafio_amanda_bot)

## Funcionalidades

O bot do Telegram oferece as seguintes funcionalidades:

- **/hoje**: Recebe a foto do dia da NASA.
- **/ontem**: Recebe a foto de ontem da NASA.
- **/dia**: Permite que o usuário escolha uma data específica para receber a foto da NASA.
- **/aleatorio**: Recebe uma foto aleatória da NASA.
- **/ajuda**: Exibe informações sobre como usar o bot.

## Estrutura do Projeto

O projeto é composto por vários arquivos:

- `main.py`: O código principal que configura e controla o bot do Telegram.
- `nasa.py`: Um módulo que consome a API da NASA para obter informações sobre a "Foto do Dia".
- `config.py`: Onde você deve armazenar suas chaves de API.
- `testes.py`: Contém testes unitários para o código.
- `requirements.txt`: Lista de dependências do projeto.

## Dificuldades

- A maior dificuldade encontrada foi a de entender como funcionava a API da NASA.
- Outra dificuldade foi a de configurar para receber a data no formato DD/MM/AAAA e converter para o formato YYYY-MM-DD, que é o formato que a API da NASA aceita.
- Por fim foi a de fazer o tratamento de erros.

## Configuração

Para executar o projeto, siga estas etapas:

1. Clone o repositório para sua máquina.
2. Instale as dependências do projeto executando `pip install -r requirements.txt`.
3. Edite o arquivo `config.py` e insira suas chaves de API do Telegram e da NASA.
4. Execute o bot usando `python main.py`.

Certifique-se de configurar seu bot no Telegram usando o BotFather e obter sua chave de API da NASA no site oficial da NASA.

## Executando Testes

Para executar os testes unitários do projeto, você pode usar o seguinte comando:

```bash
python testes.py
```

## Agradecimentos

- [Cubos Academy](https://cubos.academy/) por fornecer o desafio.
- [Adriano Binhara](https://www.instagram.com/binhara/) por fornecer o desafio.
- [NASA](https://www.nasa.gov/) por fornecer a API.
- [BotFather](https://t.me/BotFather) por fornecer a API do Telegram.

## Linguagem

[![Python 3](https://img.shields.io/badge/Python-3.12-blue?style=plastic)](https://www.python.org/)
