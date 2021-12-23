import praw
import os
import time


# environment secrets are made available to the bot instance when running on Heroku
r = praw.Reddit(
    username = "EnPassantHolyHellBot",
    password = os.environ['PASSWORD'],
    client_id = os.environ['CLIENT_ID'],
    client_secret = os.environ['CLIENT_SECRET'],
    user_agent = "EnPassantHolyHellBot by github.com/cutwell"
)

# target R/AnarchyChess comments
subr = r.subreddit('anarchychess')

def check_comment(comment):
    # try/except to handle rate limiting errors
    try:
        # detect keyphrase in body
        if "google it" in comment.body.lower():
            # traverse comment replies for punchline
            for reply in comment.replies:
                if "holy hell" in comment.replies.lower():
                    return
            
            # else, reply punchline ourselves
            source_tag = "[^(github)](https://github.com/cutwell/anarchychesscommentbot) ^|"
            body = "Holy Hell!"
            comment.reply(f"{body}\n{source_tag}")

    except praw.exceptions.APIException:
        # gracefully handle rate limiting
        print("Probably hit rate limit, pausing for 60 seconds..")
        time.sleep(60)
        print("..Resuming")

# stream new comments to sub posts
for comment in subr.stream.comments(skip_existing=True):
    check_comment(comment)  # process comment and handle correctly
