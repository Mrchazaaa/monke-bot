
import os
import jsonReader
from fbchat import Client
from fbchat.models import *
import random

GROUP_CHAT_ID = jsonReader.getValue('GROUP_CHAT_ID')
CHARLIES_ID = jsonReader.getValue('CHARLIES_ID')
USERNAME = jsonReader.getValue('USERNAME')
PASSWORD = jsonReader.getValue('PASSWORD')

message = ['']

# Subclass fbchat.Client and override required methods
class MonkeBot(Client):
    global message

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # self.mark_as_delivered(thread_id, message_object.uid)
        # self.mark_as_read(thread_id)

        print(f"my uid is {self.uid}")

        print("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        # if author_id != self.uid:
            # print("sending reply")
            # self.send(message_object, thread_id=thread_id, thread_type=thread_type)

        # if (author_id == CHARLIES_ID):
            # self.sendLocalVoiceClips('./sounds/Fart-Squeeze-Yer-Knees_Mike-Koenig.mp3', Message(text="uh oh"), thread_id=thread_id, thread_type=thread_type)
            # self.reactToMessage(message_object.uid, MessageReaction.SMILE)
        # else:
            # self.reactToMessage(message_object.uid, MessageReaction.NO)
        # if ("Emanuel" in message_object.text):
        # if (self.uid in message_object.mentions):

        #only reply to message if monkebot is mentioned
        if (next((x for x in message_object.mentions if x.thread_id == self.uid), None) != None):
            self.sendLocalVoiceClips('./sounds/Fart-Squeeze-Yer-Knees_Mike-Koenig.mp3', Message(text="uh oh"), thread_id=thread_id, thread_type=thread_type)

            # self.sendLocalVoiceClips('./sounds/Fart-Squeeze-Yer-Knees_Mike-Koenig.mp3', Message(text="uh oh"), thread_id=thread_id, thread_type=thread_type)
            # self.send(Message(text=random.choice(message)), thread_id=thread_id, thread_type=thread_type)

client = MonkeBot(USERNAME, PASSWORD)

client.listen()

