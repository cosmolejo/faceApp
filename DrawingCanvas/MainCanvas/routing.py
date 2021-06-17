# from channels.routing import route
# from MainCanvas.consumers import ws_connect, ws_disconnect


# channel_routing = [
#     route('websocket.connect', ws_connect),
#     route('websocket.disconnect', ws_disconnect),
# ]


from django.conf.urls import re_path
from MainCanvas.consumers import CanvasConsumer

websocket_urlpatterns = [
    re_path(r'ws/main/$', CanvasConsumer.as_asgi()),
]