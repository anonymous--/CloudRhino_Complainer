from configparser import ConfigParser
import json
from requests import Session


config = ConfigParser()
config.read("old_place.config")
api = "https://api.pushbullet.com/v2/pushes"
api_key = config["pushbullet"]['api']


class send_push():
    def __init__(self,code, status_message):
        self.code = code
        self.status_message = status_message
    def push(self):
        with Session() as s:
            header = {
                "Access-Token": api_key,
                "Content-Type": "application/json"
            }
            message = json.dumps({"email":config['email']['email'],
                                  "type":"note",
                                  "title":self.code,
                                  "body": self.status_message
            })
            return s.post(api, data=message, headers=header).close()