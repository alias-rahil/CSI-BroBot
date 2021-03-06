import requests
import random
from misc.text import subreddits, meme_api
from telegram.ext import CommandHandler

options = [i.lower() for i in subreddits]

def meme(update, context):
    choice = random.choice(options + ["all"])
    if choice == "all":
        api = f"{meme_api}/{choice}"
        response = requests.get(api).json()
        while response["subreddit"].lower() in options:
            response = requests.get(api).json()
    else:
        response = requests.get(f"{meme_api}/{choice}").json()
    update.message.reply_photo(response["url"], caption=response["title"])


meme_handler = CommandHandler("meme", meme)
			
			
			
			
