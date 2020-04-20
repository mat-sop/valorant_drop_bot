# valorant_drop_bot
Python script which rotates between most popular twitch valorant channels. Drop rules: `https://beta.playvalorant.com/en-us/news/announcements/day-1-closed-beta-in-eu-na-and-moving-forward/`


## Requirements

### Twitch
1. To enable valorant drops, twitch account must be connected to riot account `https://www.twitch.tv/settings/connections`
2. Two-factor authentication must be enabled to log in `https://help.twitch.tv/s/article/two-factor-authentication-with-authy`

### Selenium
1. Chrome browser is required.
2. `chromedriver` has to be in `$PATH`. It can be downloaded from `https://sites.google.com/a/chromium.org/chromedriver/downloads`
3. `chromedriver` should be modified to avoid being detected as selenium. It can by achived by `perl -pi -e 's/cdc_/dog_/g' /path/to/chromedriver`
More info: `https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver`

### Python
1. Python version - `3.8.1`
2. `pip install -r requirements.txt`


## Usage
```
python bot.py
```


## TODO
1. More info should be passed as argument than hardcoded, like max/min time to watch, etc.
2. Hosting other streamers and ending of stream should be handled.
3. Channel should be checked if valorant drop is enabled.
