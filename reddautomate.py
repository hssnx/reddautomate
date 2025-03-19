import time
import random
import praw

# --- Random Delay ---
# Sleep for a random time between 0 and 7200 seconds (up to 2 hours)
delay = random.randint(0, 7200)
print(f"Sleeping for {delay} seconds to randomize execution time...")
time.sleep(delay)

# --- Reddit API Authentication ---
# Replace the placeholders with your actual credentials.
reddit = praw.Reddit(
    client_id="<CLIENT_ID>",               # e.g., "qCgctxHC_BrAlWTvq7Vuung"
    client_secret="<CLIENT_SECRET>",       # e.g., "uUJuV9S4SapdvgbbA9394NFU31rtTxJg"
    user_agent="script:reddit-streak-bot:v1.0 (by u/<USERNAME>)",
    refresh_token="<REFRESH_TOKEN>"        # e.g., "128842474546252-U0GCzipwwtbaDsxTEaOcFHk0qlKgA0ebEQ"
)

# --- Upvoting ---
def upvote_one_post(subreddits):
    subreddit_name = random.choice(subreddits)
    subreddit = reddit.subreddit(subreddit_name)

    # Can choose between "hot", "new", "rising" ...
    for post in subreddit.new(limit=10):
        if not post.likes:
            post.upvote()
            print(f"Upvoted: {post.title}")
            print(f"Post URL: https://www.reddit.com{post.permalink}")
            print(f"Subreddit: r/{subreddit_name}")
            return

# List of subreddits
subreddits = [
    "selfhosted",
    "CompetitiveProgramming",
    "linuxadmin",
    "sysadmin",
    "cryptography",
    "unixporn",
    "homelab",
    "lowlevel",
    "programminghorror",
    "redteamsec",
]

# Run
upvote_one_post(subreddits)