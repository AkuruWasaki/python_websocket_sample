import asyncio
import websockets

async def hello():
    uri = "ws://localhost:3333"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Akuru Wasaki")
        print(await websocket.recv())

asyncio.run(hello())