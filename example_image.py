# example_image.py

import websocket
import json
from datetime import datetime
from urllib.request import urlopen

channel = 'example_python'
ws_url = 'wss://ws-old-scgsa.ondigitalocean.app'

try:
    import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    parsed_message = json.loads(message)
    if (parsed_message['channel'] == channel and parsed_message['type'] == 'IMAGE'):
        with urlopen(parsed_message['value']) as response:
            with open(parsed_message['userId'] + '.jpg', 'wb') as f:
                f.write(response.read())


def on_open(ws):
    def run(*args):
        sample_image = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAASABIAAD/4QBYRXhpZgAATU0AKgAAAAgAAgESAAMAAAABAAEAAIdpAAQAAAABAAAAJgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAEKADAAQAAAABAAAAEAAAAAD/7QA4UGhvdG9zaG9wIDMuMAA4QklNBAQAAAAAAAA4QklNBCUAAAAAABDUHYzZjwCyBOmACZjs+EJ+/8AAEQgAEAAQAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/bAEMAAgICAgICAwICAwQDAwMEBQQEBAQFBwUFBQUFBwgHBwcHBwcICAgICAgICAoKCgoKCgsLCwsLDQ0NDQ0NDQ0NDf/bAEMBAgICAwMDBgMDBg0JBwkNDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDf/dAAQAAf/aAAwDAQACEQMRAD8A2Piz4p+OH7V3iDUNZ8Pv5Pg+G/k0/RNOmv4bGK6kj5CRRzSR/arl1IZgoYjcFGOAcr4E/tD2fwE1LT7W1m8SF/tMVtr2lX00LaWFD7LhootnmxSx9UOQcjDZFe6eOrfWf2YrQeB/Emka43hrStYu9V8Oa7ocdk6TQ3hV/s1y93bz+RLEyDDoQ3cBhgj5i+B3wI8eftG/EsaxdWl0ug3GoNfazq9wm2Mo8hkkRX2qsk0mSAEHBOSAK/DMRHGU8fB0JSeKb96/T07L8OXyP9V8oq8O4zhPE080p0aeRU4XpOLtzrW3Nq+ao1ZtaTjUdneW3//Z'
        message = {
            'datetime': datetime.now().isoformat(),
            'channel': channel,
            'id': 'fizxvgdynclkojwq',
            'userId': 'davhtwsgmblecfon',
            'userName': 'Python user',
            'type': 'IMAGE',
            'value': sample_image
        }
        ws.send(json.dumps(message))

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                )
    ws.on_open = on_open
    ws.run_forever()
