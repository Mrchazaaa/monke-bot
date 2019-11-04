
import json
from fbchat import Client
from fbchat.models import *

with open('.config.json', 'r') as f:
    config_keys = json.load(f)

USERNAME = config_keys['USERNAME']
PASSWORD = config_keys['PASSWORD']

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # self.mark_as_delivered(thread_id, message_object.uid)
        # self.mark_as_read(thread_id)

        print("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        print("from: " + author_id)
        print("you are: " + self.uid)

        # If you're not the author, echo
        if author_id != self.uid:
            print("sending reply")
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = EchoBot(USERNAME, PASSWORD)

try:
    client.listen()
except KeyboardInterrupt:
    print("logging out")
    client.logout()

