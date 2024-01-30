import asyncio
import websockets
import subprocess

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")

            if message == 'connect-to-vip-server':
                print("Opening Google.com")
                # Отправляем запрос на Google.com
                subprocess.run(['termux-open-url', 'https://www.google.com'])

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {websocket.remote_address}")

if __name__ == "__main__":
    server = websockets.serve(handle_client, "localhost", 8126)

    print("WebSocket server started. Listening on ws://localhost:8126")

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
