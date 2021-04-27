from websocket import create_connection
from datetime import datetime
import json

ws = create_connection("wss://ws-old-scgsa.ondigitalocean.app")
print("Sending 'Hello, World'...")
message = {
    'datetime': datetime.now().isoformat(),
    'channel': 'example_python',
    'id': 'fizxvgdynclkojwq',
    'userId': 'davhtwsgmblecfon',
    'userName': 'Python user 2',
    'type': 'CHAT',
    # value can also be array, struct as long as it serializable
    # to JSON
    'value': '0,1000'
}
ws.send(json.dumps(message))
print("Sent")
ws.close()
