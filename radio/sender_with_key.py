from microbit import *
import radio

def caesar(key, word):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in word:
        letter = letter.upper()
        if letter in alpha:
            index = (alpha.find(letter) + key) % 26
            result += alpha[index]
        else:
            pass
    return result

radio.on()
radio.config(channel=7)
sleep(1000)

SECRET_KEY = "ABC123"

while True:
    image_name = 'HEART'  # Or any valid image name
    encrypted_message = caesar(3, image_name)
    packet = SECRET_KEY + encrypted_message
    radio.send(packet)
    sleep(5000)
