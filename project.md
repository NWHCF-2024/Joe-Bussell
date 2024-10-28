# Rock-Paper-Scissors on the Micro:bit: A Semester Capstone Project

## Abstract

The goal of this semester capstone project is to demonstrate how the micro:bit—a pocket-sized computer designed for education—can be utilized to create an interactive and multiplayer game of Rock-Paper-Scissors. This paper highlights the technologies, inputs, outputs, and communication techniques used, to serve as a guide and inspiration for high school students embarking on their own semester projects.

## Table of Contents

1. Introduction
2. Requirements and Pre-requisites
3. Inputs and Outputs
4. Communication Techniques
5. Code Architecture
6. Challenges and Lessons Learned
7. Conclusion

---

## 1. Introduction

The micro:bit is a versatile tool capable of a multitude of functions, ranging from simple displays to complex radio communications. We'll be taking advantage of its features to create a Rock-Paper-Scissors game that can be played in two modes—single-player against a computer and multiplayer via radio communication.

---

## 2. Requirements and Pre-requisites

**Hardware Required:**
- micro:bit (2 units for multiplayer)
- USB cables for programming and power

**Software Required:**
- Python editor compatible with micro:bit (e.g., Mu)

**Skills Required:**
- Basic understanding of Python programming
- Basic understanding of micro:bit's features

---

## 3. Inputs and Outputs

### Inputs

1. **Button A**: Cycles through the options (Rock, Paper, Scissors)
2. **Button B**: Confirms the selection
3. **Both Buttons**: Switches to multiplayer mode and selects host/client roles

### Outputs

1. **LED Display**: 
    - Shows various emojis to indicate winner, loser, or tie
    - Displays the current selection (Rock, Paper, Scissors)

---

## 4. Communication Techniques

### Radio Communication

The micro:bit has built-in radio communication capabilities which allow it to send and receive messages. In our project, this is used to:

1. **Announce Host and Client Status**: When a micro:bit is set to host, it sends a 'HOST' message. The client listens for this message to establish a connection.
2. **Synchronize Choices**: Once connected, each micro:bit sends its choice to the other to determine the winner.

---

## 5. Code Architecture

The code is divided into various functional blocks:

1. **Initialization**: Setting up variables and default modes.
2. **Display Logic**: Code to handle what is shown on the LED screen.
3. **Single-player Logic**: Handling interactions for single-player mode.
4. **Multiplayer Logic**: Handling radio communications and interactions for multiplayer mode.

---

## 6. Challenges and Lessons Learned

### Challenges

1. **Synchronization**: Ensuring both micro:bits are in sync was a challenge, overcome by proper message protocols.
2. **User Interface**: Limited to a 5x5 LED grid, creating recognizable icons was challenging but creatively rewarding.

### Lessons Learned

1. **State Management**: Handling different modes (single-player and multiplayer) taught us the importance of state management.
2. **Radio Communication**: Implementing this taught us the basics of wireless communication protocols.

---

## 7. Conclusion

This project serves as a hands-on introduction to hardware programming, user interface design, and wireless communications. It offers an excellent starting point for students interested in diving deeper into any of these areas. The skills and concepts learned here are not just limited to games but are applicable in broader contexts, such as IoT devices and robotics.

By following along with this project, students will gain valuable experience and knowledge that will serve them well in their academic journey and beyond.
