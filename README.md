Fitness Tracker Bot
A Python-based automation tool that generates dynamic workout reminders and motivational alerts for Telegram channels. This project demonstrates backend automation, API integration, and secure credential management using environment variables.

Features
Dynamic Content Generation: Automatically selects random workout routines and motivational quotes to keep notifications fresh.

Telegram Integration: Leverages the official Telegram Bot API to send formatted Markdown messages.

Security-First Design: Utilizes python-dotenv to manage sensitive API tokens and channel IDs, ensuring code can be shared safely without exposing credentials.

Getting Started
Prerequisites
Python 3.x installed on your machine.

A Telegram Bot Token (obtained from @BotFather).

A Telegram Channel/Group ID.

Installation
Clone the repository:

Bash
git clone https://github.com/B0o07/fitness-tracker-bot.git
cd fitness-tracker-bot
Install the required dependencies:

Bash
pip install requests python-dotenv
Configure environment variables:

Create a file named .env in the project root directory.

Add your credentials to this file:

Plaintext
TELEGRAM_BOT_TOKEN=your_actual_token_here
TELEGRAM_CHAT_ID=@your_channel_id
Usage
Execute the bot script to send a notification:

Bash
python index.py
Security Notice
Never commit your .env file to version control. This repository includes a .gitignore file configured to automatically exclude the .env file, protecting your sensitive API keys from being exposed publicly on GitHub.

License
This project is open-source and available for customization.