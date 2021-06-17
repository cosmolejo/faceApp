# Import JSON module
import json

# Import WebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


from PIL import Image
import base64
from io import BytesIO
import cairosvg

DPI = 96
_scale = 1

# Define the consumer class to send the data through WebsocketConsumer
class CanvasConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 1111
        self.room_group_name = "model_%s" % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        message = response["image"]
        race = response['race']  
        print(race)

        byte_data = base64.b64decode(message)
        byte_data = cairosvg.svg2svg(byte_data, dpi=(DPI / _scale))
        _bytes = cairosvg.svg2png(byte_data)
        byte_io = BytesIO(_bytes)
        img = Image.open(byte_io)
        img = img.resize((256, 256))
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
        # background.show()


        buffered = BytesIO()
        background.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "model_response", "image": img_str.decode("utf-8")}
        )

    def model_response(self, event):
        """Receive message from room group"""
        message = event["image"]

        print("respuesta")
        # Send message to WebSocket
        self.send(text_data=json.dumps({"image": message}))
