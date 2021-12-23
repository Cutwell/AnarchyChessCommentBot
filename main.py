import praw
import os
import time

# init reddit bot instance
# environment secrets are made available to the bot instance when running on Heroku
r = praw.Reddit(
    username = "EnPassantHolyHellBot",
    password = os.environ['password'],
    client_id = os.environ['client_id'],
    client_secret = os.environ['client_secret'],
    user_agent = "EnPassantHolyHellBot by github.com/cutwell"
    )

subr = r.subreddit('anarchychess')

# stream new comments to sub posts
for comment in subr.stream.comments(skip_existing=True):
    try:
        # detect joke setup (string "google it" in a comment body)
        if "google it" in comment.body:
            # comment punchline
            comment.reply("holy hell")
    except praw.exceptions.APIException:
        # gracefully pause when hitting wait limit
        print("Probably a rate limit, waiting 60 seconds..")
        time.sleep(60)
        print("..Resuming")