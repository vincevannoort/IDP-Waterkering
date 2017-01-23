from channels.routing import route
from waterkering.consumers import connect, update, disconnect

channel_routing = [
    route("websocket.connect", connect),
    route("websocket.receive", update),
    route("websocket.disconnect", disconnect),
]