import asyncio
import websockets
import subprocess
import os
import time

def colored_text(text, color):
    colors = {
        'reset': '\033[0m',
        'info': '\033[94m',         # Blue
        'warn': '\033[93m',         # Yellow
        'success': '\033[92m',      # Bright Green
        'bright_cyan': '\033[96m'   # Bright Cyan
    }
    return f"{colors[color]}{text}{colors['reset']}"

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")

            if message == 'connect-to-vip-server':

                pid_result = subprocess.run(['pgrep', '-f', 'com.roblox.client'], stdout=subprocess.PIPE, text=True)
                pid = pid_result.stdout.strip()

                if pid:
                    print(colored_text(f"Closing application with PID: {pid}", 'warn'))
                    subprocess.run(['kill', pid])

                time.sleep(5)  # Заменено на правильный вызов функции sleep из модуля time

                print(colored_text("Opening link...", 'info'))
                subprocess.run(['termux-open-url', 'https://www.roblox.com/games/3260590327?privateServerLinkCode=45922069851868244203416146497318'])

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {websocket.remote_address}")

if __name__ == "__main__":
    subprocess.run(['clear'])
    print(colored_text('''
   ___  _____   _______  ______
  / _ \/ __/ | / /  _/ |/_/_  /
 / // / _/ | |/ // /_>  <  / / 
/____/___/ |___/___/_/|_| /_/ 
     github.com/DEVIX7
    ''', 'bright_cyan'))

    try:
        import websockets
    except ImportError:
        print(colored_text("Module 'websockets' not found. Auto-installing...", 'warn'))
        subprocess.run(['pip', 'install', 'websockets'])

    server = websockets.serve(handle_client, "localhost", 8126)

    print(colored_text("WebSocket server started. Listening on ws://localhost:8126", 'success'))

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
