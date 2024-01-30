import subprocess

required_modules = ['asyncio', 'websockets', 'webbrowser']

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Module '{module}' not found. Installing...")
        subprocess.run(['pkg', 'install', f'python-{module.lower()}'], check=True)
        
async def handle_client(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")

            if message == 'connect-to-vip-server':
                print("Opening Google.com")

                subprocess.run(['am', 'start', '--user', '0', '-a', 'android.intent.action.VIEW', '-d', 'https://www.google.com'], check=True)

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {websocket.remote_address}")

if __name__ == "__main__":
    server = websockets.serve(handle_client, "localhost", 8126)

    print("WebSocket server started. Listening on ws://localhost:8126")

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
