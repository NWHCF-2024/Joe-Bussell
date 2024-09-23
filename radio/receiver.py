# Receiver Code
from microbit import *
import radio

# Initialize the radio
radio.on()
radio.config(channel=7)  # Must match the transmitter's channel

receiving = False  # Control variable for receiving data

def send_command(command):
    radio.send(command)

while True:
    # Check for button presses to start or stop data reception
    if button_a.was_pressed():
        send_command('start')
        receiving = True
    if button_b.was_pressed():
        send_command('stop')
        receiving = False

    if receiving:
        # Receive data from the transmitter
        incoming = radio.receive()
        if incoming:
            try:
                # Parse the incoming data
                temp_str, voltage_str = incoming.split(',')
                temp = int(temp_str)
                voltage = float(voltage_str)
                
                # Display the data
                display.scroll("Temp:{}C Voltage:{}V".format(temp, voltage))
            except:
                # Handle any parsing errors
                pass
    else:
        sleep(100)
