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

# Custom exception thrown during middleware execution to indicate that no further middleware should be processed
class BreakMiddlewareChain(Exception):
   def __init__(self, arg):
      self.args = arg

# Subclass fbchat.Client and override required methods
class MonkeBot(Client):
    global message

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        
        #print(f"my uid is {self.uid}")
        print("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        #only reply to messages that: 
        # - mention Emanuel
        # - are DMs sent by charlie howlett (for testing)
        # - are not sent by Emanuel (do not respond to your own messages)
        if ((next((x for x in message_object.mentions if x.thread_id == self.uid), None) != None or
            author_id == CHARLIES_ID) and 
            author_id != self.uid):

            try:
                # React to sender message
                self.reactToMessage(message_object.uid, MessageReaction.SMILE)

                self.recordings(message_object, thread_id, thread_type)

                # Defines default behaviour so must be last (could change default behaviour to seperate method)
                self.phrases(message_object, thread_id, thread_type)
            except BreakMiddlewareChain:
                return

    
    def phrases(self, message_object, thread_id, thread_type):
        #check to see if phrases are being added
        if ("add phrase" in message_object.text):
            #add phrase to database
            phraseToAdd = message_object.text.split("add phrase", 1)[1]
            raise BreakMiddlewareChain
        #check to see if phrases are being requested (current default behaviour, should probably refactor)
        else:
            messagesFromDB = ["UH OH", "STINKY", "POOPY", "HAHA"] #replace with DB call
            self.send(Message(text=random.choice(messagesFromDB)), thread_id=thread_id, thread_type=thread_type)

    def recordings(self, message_object, thread_id, thread_type):
        #check to see if a recording is being added
        #check to see if a recording is being requested
        if ("stinky" in message_object.text):
            # send fart noise
            self.sendLocalVoiceClips('./sounds/Fart-Squeeze-Yer-Knees_Mike-Koenig.mp3', Message(text="uh oh"), thread_id=thread_id, thread_type=thread_type)
            raise BreakMiddlewareChain

client = MonkeBot(USERNAME, PASSWORD)
client.listen()
