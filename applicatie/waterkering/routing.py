from channels.routing import route
from waterkering.consumers import ws_add, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", connect),
    route("websocket.receive", update),
    route("websocket.disconnect", disconnect),
]