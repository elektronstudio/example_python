import websocket
import json
from datetime import datetime

# Pick a channel name. It has to be same in Python and Javascript
# and it's also referred in testing URL at  https://elektron.art/example_python

channel = 'example_python'

ws_url = 'wss://ws-old-scgsa.ondigitalocean.app'

try:
    import thread
except ImportError:
    import _thread as thread


# Incoming message in JSON format

def on_message(ws, message):
    parsed_message = json.loads(message)
    # For chat messages type is 'CHAT'
    if (parsed_message['channel'] == channel and parsed_message['type'] == 'CHAT'):
        print(parsed_message)

# Outgoing message in JSON format

# https://pypi.org/project/websocket-client/


def on_open(ws):
    def run(*args):
        # All the fields are optional except channel, type and value
        message = {
            'datetime': datetime.now().isoformat(),
            'channel': channel,
            'id': 'fizxvgdynclkojwq',
            'userId': 'davhtwsgmblecfon',
            'userName': 'Python user',
            'type': 'CHAT',
            # value can also be array, struct as long as it serializable
            # to JSON
            'value': '0,1000'
        }
        ws.send(json.dumps(message))

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                )
    ws.on_open = on_open
    ws.run_forever()
