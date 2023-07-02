# pathfinder-bot
Python 3 script that checks if a specified path exists and sends a Telegram message on the state.<br>
I created this because my External hard drive disconnects sometimes and wanted to know when so i can fix it.

## **Why Telegram?**
>I found it easy to use and can send a notification to my phone

# Setup

## **Configuring uservariables.py**
I used [this article](https://12ft.io/proxy?q=https%3A%2F%2Fmedium.com%2Fcodex%2Fusing-python-to-send-telegram-messages-in-3-simple-steps-419a8b5e5e2) to find out how to create a Telegram bot and send a message with Python.
### Getting chat-id
You can get your chat-id by messaging /start to @rawdatabot on telegram
### Setting path variable
When adding your **path variable** make sure to change backslashes( \ ) to forwardslashes( / )

## Setting up service(Debian)
i personally used this unix stackexchange [page](https://unix.stackexchange.com/questions/634410/start-python-script-at-startup) to figure it out
