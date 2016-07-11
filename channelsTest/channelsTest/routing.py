# In routing.py
from channels.routing import route
channel_routing = [
    route("http.request", "chtest.controllers.consumers.http_consumer"),
]
