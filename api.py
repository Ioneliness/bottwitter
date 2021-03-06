import main
from twitter import api
from main import create_image_end
import time

bot_user = '@BotThumb'


def get_last_seen_id():
    with open('txts/last_seen_id.txt', 'r') as file:
        return file.read().splitlines()[0]


def store_last_seen_id(tweet_id):
    with open('txts/last_seen_id.txt', 'w') as file:
        file.write(str(tweet_id))


import tweepy 

def get_timeline():
    last_seen_id = get_last_seen_id()
    timeline = api.search('#botthumb', since_id=last_seen_id, tweet_mode='extended')
    for tweet in reversed(timeline):
        try:
            tweet_id = tweet.id
            text = tweet.full_text.replace(bot_user, '')
            if '#botthumb' in text.lower():
                text = tweet.full_text
                splited = text.split()
                new_text = ''
                for part in splited:
                    if '#' not in part and bot_user not in part and '@' not in part:
                        new_text += part +' '
                if new_text:
                    create_image_end(new_text)
                    author_user = f'@{tweet.author.screen_name}'
                    text = author_user
                    api.update_with_media('images/atual.png', text, in_reply_to_status_id=tweet_id)
                    store_last_seen_id(tweet_id)
        except Exception as e:
            print(e)
            tweet_id = tweet.id
            store_last_seen_id(tweet_id)

def get_mentions():
    last_seen_id = get_last_seen_id()
    timeline = api.mentions_timeline(since_id=last_seen_id, tweet_mode='extended')
    for tweet in reversed(timeline):
        try:
            tweet_id = tweet.id
            text = tweet.text.replace(bot_user, '')
            create_image_end(text)
            author_user = f'@{tweet.author.screen_name}'
            text = author_user
            api.update_with_media('images/atual.png', text, in_reply_to_status_id=tweet_id)
            store_last_seen_id(tweet_id)
            break
        except Exception as e:
            print(e)
            tweet_id = tweet.id
            store_last_seen_id(tweet_id)

if __name__ == '__main__':
    while True:
        try:
            get_timeline()
            get_mentions()
            time.sleep(30)
        except Exception as e:
            print(e)
