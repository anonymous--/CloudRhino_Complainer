import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser
from datetime import datetime
from pushbullet import send_push
import complainer


config = ConfigParser()
config.read('old_place.config')
old_place = int(config['place']['old_place'])
old_day = datetime.utcfromtimestamp(int(config['place']['date'])).day
today = datetime.utcnow()
old_date = datetime.fromtimestamp(int(config['place']['date']))
days = today.day - old_date.day


def get_from_web():
    api = 'https://www.cloudrino.net/index.php?error=1&email='
    raw = requests.get(api+config['email']['email']).text
    soup = BeautifulSoup(raw, 'html5lib')
    my_place = int(str(soup.find_all('h1')).replace(
        '[<h1>#', '').replace('#', '').replace('</h1>]', '').replace("'", "").split(' of ')[0])
    return my_place


def update_config():
    with open('old_place.config', 'w') as update:
        config['place']['old_place'] = str(get_from_web())
        config['place']['date'] = str(int(datetime.utcnow().timestamp()))
        config.write(update)


complain = complainer.complain(days, get_from_web(), old_date, old_place)


def run():
    if get_from_web() == old_place:

        if days > 1:
            send_push('Success', "send haven't moved message to the twitter.").push()
            update_config()
            return complain.not_moved()

    elif old_place < get_from_web():
        if days > 1:
            send_push('Success', "sent the moved back  message to the twitter.").push()
            update_config()
            return complain.moved_back()

    elif old_place > get_from_web():
        if days > 1:
            send_push('Success', "sent the moved up message to the twitter.").push()
            update_config()
            return complain.moved_up()