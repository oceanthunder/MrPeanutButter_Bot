# MrPeanutButter-Bot

MrPeanutButter-Bot is a Reddit bot designed to interact with the r/BoJackHorseman subreddit by monitoring comments for mentions of the character "Mr. Peanutbutter" and "Erica" and responding with predefined messages and images related to the character. The bot includes functionality to manage Reddit API rate limits to ensure it operates efficiently without violating Reddit’s guidelines.

## Features

- Monitors comments in the r/BoJackHorseman subreddit.
- Responds automatically to any mention of "Mr. Peanutbutter" or "Erica."
- Handles Reddit API rate limits to avoid overuse of resources.
- Customizable subreddit interactions.

## Prerequisites

Before running MrPeanutButter-Bot, you will need to set up a configuration file to authenticate the bot with the Reddit API. The required credentials can be obtained by registering an application on Reddit via the [Reddit Apps page](https://www.reddit.com/prefs/apps).

### Required Credentials

To run the bot, you will need the following information:

- **Reddit Username**
- **Reddit Password**
- **Client ID**: This is generated when you register your application on Reddit.
- **Client Secret**: Also generated during the application registration process.

## Setup and Installation

### 1. Clone the Repository
First, clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/oceanthunder/MrPeanutButter-Bot.git
```

### 2. Create a `config.py` File
In the root of the repository, create a `config.py` file and populate it with your Reddit credentials:
```python
username = 'your_reddit_username'
password = 'your_reddit_password'
client_id = 'your_reddit_client_id'
client_secret = 'your_reddit_client_secret'
```

### 3. Install Required Packages
Install the necessary Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Modify Subreddit (Optional)
If you wish to change the subreddit the bot interacts with, modify the following line in `bot.py`:
```python
for comment in r.subreddit('BoJackHorseman').comments(limit=100):
```
You can replace `'BoJackHorseman'` with the name of any subreddit you prefer.

### 5. Run the Bot
Once everything is set up, simply run the bot using:
```bash
python bot.py
```

The bot will start monitoring the specified subreddit and respond to comments mentioning "Mr. Peanutbutter."

## Handling Reddit Rate Limits

The bot is designed to handle Reddit API rate limits efficiently to avoid being temporarily banned or restricted by Reddit for excessive requests. The bot monitors the rate limits and adapts its behavior accordingly, ensuring smooth and safe operation.

## Contribution Guidelines

We welcome contributions to improve MrPeanutButter-Bot. Please see the [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get involved.

---
