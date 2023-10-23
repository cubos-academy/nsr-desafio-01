# 🌌 NasaApodImages Bot

[![Python Version](https://img.shields.io/badge/python-3.9.6-blue.svg)](https://www.python.org/downloads/release/python-396/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code Formatter: isort](https://img.shields.io/badge/code%20formatter-isort-000000.svg)](https://pycqa.github.io/isort/)
[![Commitizen Friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Clean Code Principles](https://img.shields.io/badge/principles-clean--code-blue.svg)](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
[![SOLID Principles](https://img.shields.io/badge/principles-SOLID-blue.svg)](https://en.wikipedia.org/wiki/SOLID)

This bot integrates with the NASA API and the Telegram API to provide users with the Astronomy Picture of the Day (APOD) and more. It allows users to request APOD images from specific dates and provides various other functionalities.

## Installation

1. Clone the repository from GitHub:

```bash
git clone https://github.com/aar7hur/NasaApoImages.git


## 🛠️ Installation

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/aar7hur/nsr-desafio-01.git
   ```

2. Install required dependencies:

   ```bash
   pip install -e .
   ```

3. Set up the necessary environment variables in a .env file:

   ```bash
   NASA_API_KEY=your_nasa_api_key
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   ```

4. Run the script using the provided entry point.

   ```bash
   python3 -m nsrdesafio01.src.main --run
   ```
    
   or 
   ```bash
   make run_telegram_bot_listener
   ```

## 🚀 Features

1. Fetch the Astronomy Picture of the Day (APOD) from NASA.
2. Send the APOD image to a chat on Telegram automatically.
3. Allow users to request the APOD image from a specific date by sending a message to the bot.
4. Implement additional optional commands for a more comprehensive user experience.

## 🚧 Challenges Faced

During the development of the NasaApoImages bot, we encountered several challenges, including:

- Integrating with the NASA and Telegram APIs to ensure smooth communication and data retrieval.
- Ensuring the continuous polling for updates from Telegram and processing the latest messages.
- Managing the complexities of handling various user commands and requests.
- Managing and maintaining the codebase and ensuring code quality and best practices.

## 🔜 Upcoming Features

Please note that some of the required features are still under development. These include:

- Sending the APOD image daily to each bot subscriber.
- Adding the ability to filter images based on specific dates.

## 🔧 Custom API Clients

Both the NASA API client and the Telegram API client were developed from scratch without using any plug-and-play libraries. This approach allowed to have complete control over the functionalities and tailor the clients to our specific needs.
