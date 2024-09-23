# Transmitter Code
from microbit import *
import radio

# Initialize the radio
radio.on()
radio.config(channel=7)  # Ensure both micro:bits are on the same channel

transmitting = False  # Control variable for transmission

while True:
    # Listen for start/stop commands from the receiver
    incoming = radio.receive()
    if incoming == 'start':
        transmitting = True
    elif incoming == 'stop':
        transmitting = False

    if transmitting:
        # Measure temperature
        temp = temperature()
        
        # Measure voltage on pin0
        scale = 3.3 / 1024  # Micro:bit uses 3.3V logic levels
        voltage = pin0.read_analog() * scale
        voltage = round(voltage, 2)
        
        # Prepare data string
        data = "{},{}".format(temp, voltage)
        
        # Send data via radio
        radio.send(data)
        
        # Small delay between transmissions
        sleep(1000)  # Transmit every 1 second
    else:
        sleep(100)
