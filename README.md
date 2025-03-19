# Reddit Streak Bot

**Description:**  
This Python script uses PRAW and Reddit's OAuth2 to upvote one new post daily from a specified list of subreddits to keep your Reddit streak alive. It’s designed for macOS and can run via launchd—even if your laptop was off at the scheduled time. A random delay is included to mimic human behavior.

## Setup

1. **Reddit App:**  
   Create a Reddit API script app with redirect URI `http://127.0.0.1/` and obtain your client ID and secret.

2. **OAuth2 Flow:**  
   Follow the authorization process to get a refresh token with the scopes `identity vote read`.

3. **Configuration:**  
   Update `redautomate.py` with your credentials.

4. **Scheduling (macOS):**  
   Copy the provided plist file (`com.example.redautomate.plist`) into `~/Library/LaunchAgents/` and load it: `launchctl load ~/Library/LaunchAgents/com.example.redautomate.plist`

## Usage

Activate your virtual environment and run: `python3 redautomate.py` Logs are saved in `/tmp/redautomate.out` and `/tmp/redautomate.err`.

*Note:* Update paths in `com.example.redautomate.plist` to point to the Python interpreter in your virtual environment and the correct script path.