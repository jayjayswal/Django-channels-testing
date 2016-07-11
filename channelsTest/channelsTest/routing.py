# In routing.py
from channels.routing import route
from chtest.controllers.consumers import ws_add, ws_message, ws_disconnect

channel_routing = [
    #route("http.request", "chtest.controllers.consumers.http_consumer"),
    # route("websocket.receive", ws_message,path=r"^/firstConnect"),
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]
