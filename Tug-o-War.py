from microbit import *
import music

def play_round():
    A_presses = 0  # Track A button presses, initialized to 0
    B_presses = 0  # Track B button presses, initialized to 0
    
    while True:
        sleep(100)  # Give 0.1 seconds for presses to register
        A_presses += button_a.get_presses()  # Add A button presses
        B_presses += button_b.get_presses()  # Add B button presses

        if A_presses == B_presses:  # If they are equal
            display.clear()  # Clear screen
            display.set_pixel(2, 2, 9)  # Dot in the middle
        
        elif A_presses + 1 == B_presses:  # If B has 1 more press
            display.clear()  # Clear screen
            display.set_pixel(3, 2, 9)  # Dot 1 closer to B

        elif A_presses - 1 == B_presses:  # If A has 1 more press
            display.clear()  # Clear screen
            display.set_pixel(1, 2, 9)  # Dot 1 closer to A

        elif A_presses + 2 == B_presses:  # If B has 2 more presses
            display.clear()  # Clear screen
            display.set_pixel(4, 2, 9)  # Dot 2 closer to B

        elif A_presses - 2 == B_presses:  # If A has 2 more presses
            display.clear()  # Clear screen
            display.set_pixel(0, 2, 9)  # Dot 2 closer to A
        
        elif A_presses >= B_presses + 3:  # If A wins by >3 presses
            display.clear()  # Clear screen
            display.show(Image.HAPPY)  # Show smiley face
            music.play(music.BA_DING)  # Celebratory sound
            sleep(500)  # Wait half a second
            display.scroll('A wins!')  # Scroll 'A wins'
            music.play(music.POWER_UP)  # Victory tune for A
            return 'A'  # Return 'A' indicating A won the round

        elif B_presses >= A_presses + 3:  # If B wins by >3 presses
            display.clear()  # Clear screen
            display.show(Image.HAPPY)  # Show smiley face
            music.play(music.BA_DING)  # Celebratory sound
            sleep(500)  # Wait half a second
            display.scroll('B wins!')  # Scroll 'B wins'
            music.play(music.POWER_UP)  # Victory tune for B
            return 'B'  # Return 'B' indicating B won the round

def play_best_of_three():
    A_wins = 0  # Track the number of wins for player A
    B_wins = 0  # Track the number of wins for player B

    while A_wins < 2 and B_wins < 2:  # Continue until one player wins 2 rounds
        winner = play_round()  # Play a round and determine the winner
        if winner == 'A':
            A_wins += 1
        else:
            B_wins += 1
        
        if A_wins == 2:  # If A wins 2 rounds, display final result
            display.clear()
            display.scroll('A wins the game!')
            music.play(music.ENTERTAINER)  # Play final victory tune for A
        elif B_wins == 2:  # If B wins 2 rounds, display final result
            display.clear()
            display.scroll('B wins the game!')
            music.play(music.ENTERTAINER)  # Play final victory tune for B

while True:
    play_best_of_three()  # Play the best of 3 series

    # Wait for a button press to start a new game
    display.clear()
    display.scroll('Press A or B for new game')

    # Poll for button press to start a new game
    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            music.play(music.JUMP_UP)  # Sound for starting a new game
            break  # Break out of the loop and start a new game
