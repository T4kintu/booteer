# Import the necessary libraries
import pycraft
import threading
import random
import time

# Ask the user to enter the address and port of the Minecraft server
host = input("Enter the address of the Minecraft server: ")
port = int(input("Enter the port of the Minecraft server: "))

# Ask the user to enter the delay between each bot
delay = float(input("Enter the delay between each bot (in seconds): "))

# Ask the user to enter the version of the Minecraft protocol
version = int(input("Enter the version of the Minecraft protocol: "))

# Ask the user to enter the number of bots they want to send
num_bots = int(input("Enter the number of bots you want to send: "))

# Define a function that creates a bot and connects to the server
def create_bot(name, proxy):
    # Create an instance of the MinecraftClient class from pycraft
    client = pycraft.MinecraftClient()
    # Set the name of the bot
    client.username = name
    # Set the proxy of the bot
    client.proxy = proxy
    # Set the version of the Minecraft protocol
    client.version = version
    # Try to connect to the server
    try:
        client.connect(host, port)
        # Send a message to the chat
        client.chat("I am " + name + ", a bot!")
        # Disconnect from the server
        client.disconnect()
    except Exception as e:
        # Print the error if it occurs
        print(e)

# Create a list of threads for the bots
threads = []

# Read the files from nick.txt and proxi.txt and save them in lists
with open("nick.txt", "r") as f:
    names = f.read().splitlines()
with open("proxi.txt", "r") as f:
    proxies = f.read().splitlines()

# Create the bots and add them to the list of threads
for i in range(num_bots):
    # Choose a random name and proxy from the lists
    name = random.choice(names)
    proxy = random.choice(proxies)
    # Create a thread with the function create_bot and the arguments name and proxy
    t = threading.Thread(target=create_bot, args=(name, proxy))
    threads.append(t)

# Start the threads with a delay between each one
for t in threads:
    t.start()
    time.sleep(delay)

# Wait for the threads to finish
for t in threads:
    t.join()

# Print a completion message
print("You have sent " + str(num_bots) + " bots to the Minecraft server.")
