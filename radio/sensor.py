# Sensor Code
from microbit import *
import radio
import random

def generate_unique_id():
    seed = running_time() + temperature() + accelerometer.get_x()
    random.seed(seed)
    uid = ''.join([chr(random.randint(65, 90)) for _ in range(6)])
    return uid

unique_id = generate_unique_id()

radio.on()
radio.config(channel=7)  # Use a common channel

while True:
    # Measure temperature
    temp = temperature()
    
    # Measure voltage
    scale = 3.3 / 1024
    voltage = pin0.read_analog() * scale
    voltage = round(voltage, 2)
    
    # Prepare data
    data = "{},{},{}".format(unique_id, temp, voltage)
    
    # Send data
    radio.send(data)
    
    # Random delay to reduce collisions
    sleep(random.randint(900, 1100))
