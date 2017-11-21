import asyncio

import websockets

import bot


@asyncio.coroutine
def handler(websocket, path):
    while True:
        try:
            msg = yield from websocket.recv()
            reply = bot.reply(msg)
            yield from websocket.send(reply)
        except websockets.ConnectionClosed:
            return

start_server = websockets.serve(handler, '0.0.0.0', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
