import pyrebase
import pygame
import serial
import time

config = {
    "apiKey": "AIzaSyBuQKF1M7jZp1NqSLuhZGiTVyFOMX4zUxE",
    "authDomain": "mars-8c17e.firebaseapp.com",
    "databaseURL": "https://mars-8c17e.firebaseio.com",
    "storageBucket": "mars-8c17e.appspot.com",
    "serviceAccount": "mars-8c17e-firebase-adminsdk-vxm71-3ca4b4127e.json"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
db = firebase.database()
paused = False

pygame.mixer.init()

try:
    arduino = serial.Serial('COM6', 57600)
except:
    print("Failed to connect on COM6")


def getMessage():
    message = db.child().get()

    if (message.val() != None):
        storage.child("message.wav").download("message.wav")
        db.child().remove()

        arduino.write(b'A')

        pygame.mixer.music.load('mensagem.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)

        time.sleep(5)

        while arduino.read() != b'4':
            arduino.read()

        playMessage()

def playMessage():
    pygame.mixer.music.load("message.wav")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

while 1:
    getMessage()

    if arduino.in_waiting == True:
        x = arduino.read()

        if x == b'1':
            playMessage()

        elif x == b'2':
            pause()

        elif x == b'3':
            unpause()