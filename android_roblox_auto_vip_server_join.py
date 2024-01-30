import asyncio
import websockets
import subprocess

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")

            if message == 'connect-to-vip-server':
                print("Opening link...")
                subprocess.run(['termux-open-url', 'https://www.roblox.com/games/3260590327?privateServerLinkCode=45922069851868244203416146497318'])

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {websocket.remote_address}")

if __name__ == "__main__":
    print('''
   ___  _____   _______  ______
  / _ \/ __/ | / /  _/ |/_/_  /
 / // / _/ | |/ // /_>  <  / / 
/____/___/ |___/___/_/|_| /_/ 
     github.com/DEVIX7
    ''')
    try:
        import websockets
    except ImportError:
        print("Module 'websockets' not found. Auto-installing...")
        subprocess.run(['pip', 'install', 'websockets'])

    server = websockets.serve(handle_client, "localhost", 8126)

    print("WebSocket server started. Listening on ws://localhost:8126")

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
