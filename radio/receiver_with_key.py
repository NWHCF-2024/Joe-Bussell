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
            # Ignore non-alphabetic characters
            pass
    return result

valid_images = [ ... ]  # Same as before

radio.on()
radio.config(channel=7)
sleep(1000)

# Pre-shared secret key for authentication
SECRET_KEY = "ABC123"

while True:
    packet = radio.receive()
    if packet:
        print("Received encrypted:", packet)
        # Check if the packet contains the secret key
        if packet.startswith(SECRET_KEY):
            # Remove the secret key before decryption
            encrypted_message = packet[len(SECRET_KEY):]
            decrypted_packet = caesar(-3, encrypted_message)
            print("Decrypted packet:", decrypted_packet)
            
            if decrypted_packet in valid_images:
                try:
                    image_to_show = getattr(Image, decrypted_packet)
                    display.show(image_to_show)
                    sleep(2500)
                except Exception as e:
                    print("Error displaying image:", e)
            else:
                print("Invalid image name:", decrypted_packet)
                display.show(Image.NO)
                sleep(1000)
        else:
            # Packet does not contain the secret key
            print("Received packet without valid secret key.")
            # Ignore the packet or handle accordingly
            pass
