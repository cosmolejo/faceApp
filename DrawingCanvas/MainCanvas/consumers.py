# Import JSON module
import json
# Import WebsocketConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncJsonWebsocketConsumer
# Import datetime module
from datetime import datetime
# Import  sleep module
from time import sleep


# Define the consumer class to send the data through WebsocketConsumer
class CanvasConsumer(WebsocketConsumer):
    def connect(self):
        #await self.channel_layer.group_add()

        self.accept()
        while(True):
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)
    
    def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        if event == 'SUBMIT':
            print(message)
            
        

    def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        # await self.send(text_data=json.dumps({
        #     "payload": res,
        # }))