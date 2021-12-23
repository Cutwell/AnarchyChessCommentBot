import praw
import os

r = praw.Reddit(
    username = "EnPassantHolyHellBot",
    password = os.environ['password'],
    client_id = os.environ['client_id'],
    client_secret = os.environ['client_secret'],
    user_agent = "EnPassantHolyHellBot by github.com/cutwell"
    )

subr = r.subreddit('anarchychess')  # this chooses a subreddit you want to get comments from

for comment in subr.stream.comments(skip_existing=True):    # this iterates through the comments from that subreddit as new ones are coming in
    try:
        if "google it" in comment.body:     # "!bot" is the keyword in this case. replace "bot" with your keyword
            comment.reply("holy hell")      # this is what your bot replies to the comment that has the keyword
    except praw.exceptions.APIException:    # Reddit may have rate limits, this prevents your bot from dying due to rate limits
        print("probably a rate limit...")