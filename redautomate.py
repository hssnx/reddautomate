import praw
import random

REFRESH_TOKEN = "your_refresh_token_here"

reddit = praw.Reddit(
    client_id="your_client_id_here",
    client_secret="your_client_secret_here",
    user_agent="script:streak-bot:v1.0 (by u/username)",
    refresh_token=REFRESH_TOKEN
)

def upvote_one_post(subreddits):
    subreddit_name = random.choice(subreddits)
    subreddit = reddit.subreddit(subreddit_name)

    for post in subreddit.new(limit=10):
        if not post.likes:
            post.upvote()
            print(f"✅ Upvoted: {post.title}")
            print(f"🔗 Post URL: https://www.reddit.com{post.permalink}")
            print(f"📌 Subreddit: r/{subreddit_name}")
            return

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

upvote_one_post(subreddits)