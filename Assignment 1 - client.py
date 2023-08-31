import websockets
import asyncio

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    
    try:
        # Connect to the server
        async with websockets.connect(url) as ws:
            # Send a greeting message
            await ws.send("Hello Server!")
            
            # Stay alive for a certain number of iterations or until a condition is met
            for i in range(10):  # Replace 10 with the desired number of iterations
                msg = await ws.recv()
                print(msg)
                
                # Add your message handling logic here
                
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed unexpectedly: {e}")

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())

