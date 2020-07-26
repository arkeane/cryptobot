# cryptobot

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LZDKH4PL5Z3XN&source=url)

Get crypto prices, set reminders and much more...
TelegramBOT Based on CoinbasePro API 

## Use it at [BOT](https://t.me/lcrypto_bot) or @lcrypto_bot

## Run the bot yourself

1. clone the repository and cd inside it.

    ```bash
    git clone https://github.com/arkeane/cryptobot.git
    cd crytptobot
    ```

2. create a file named bot_token.txt inside the repository folder and paste there your Telegram Bot token (obtain it from BotFather).

    ```bash
    touch bot_token.txt
    echo "TOKEN" > bot_token.txt
    ````

3. Run the Bot (Two ways):

    1. Install the required software and run the bot

        ```bash
        pip install -r requirements.txt
        python bot.py
        ```

    2. Use Docker (recommended)
        Install docker and then:

        ```bash
        docker build -t cryptobot .
        docker run -dit --restart unless-stopped --name cryptobot_telegram cryptobot
        ```
