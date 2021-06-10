import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import MainCanvas.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DrawingCanvas.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            MainCanvas.routing.websocket_urlpatterns
        )
    ),
})


