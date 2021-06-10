# from channels.routing import route
# from MainCanvas.consumers import ws_connect, ws_disconnect


# channel_routing = [
#     route('websocket.connect', ws_connect),
#     route('websocket.disconnect', ws_disconnect),
# ]


from django.conf.urls import url
from MainCanvas.consumers import CanvasConsumer

websocket_urlpatterns = [
    url('main/', CanvasConsumer.as_asgi()),
]