# Receiver Code
from microbit import *
import radio

radio.on()
radio.config(channel=7)  # Same channel as sensors

while True:
    incoming = radio.receive()
    if incoming:
        try:
            # Parse the message
            unique_id, temp_str, voltage_str = incoming.split(',')
            temp = int(temp_str)
            voltage = float(voltage_str)
            
            # Process or display data
            display.scroll("{} T:{}C V:{}V".format(unique_id, temp, voltage))
            
        except:
            # Handle parsing errors
            pass
    sleep(50)
