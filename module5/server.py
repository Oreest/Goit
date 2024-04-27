import asyncio
import websockets
from main import get_currency


async def hello(websocket):
    name = await websocket.recv()
    if name.lower() == 'exchange':
        await websocket.send(get_currency(0))

    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
