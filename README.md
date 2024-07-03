To run this bot you'll need to create a config.py file in which you have to add the following:

username = 'your_reddit_username'
password = 'your_reddit_password'
client_id = 'your_reddit_client_id'
client_secret = 'your_reddit_client_secret'

If you want to change the subreddit the bot interacts with, modify the following line in bot.py:
   for comment in r.subreddit('BoJackHorseman').comments(limit=100):
   
The bot is designed to handle rate limits and avoid getting banned.

After this run bot.py and it should work
