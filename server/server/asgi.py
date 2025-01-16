import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import userApp.routing
from django.urls import path
from userApp import consumers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # userApp.routing.websocket_urlpatterns
            path('ws/chat/', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
