import wave
import pyaudio
import pyrebase
from PyQt5 import QtWidgets
from playsound import playsound
from ui_recorder import Ui_Recorder

class RecorderWindow(QtWidgets.QMainWindow, Ui_Recorder):
    def __init__(self, parent=None):
        super(RecorderWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.record_message)
        self.pushButton_3.clicked.connect(self.play_message)
        self.pushButton_4.clicked.connect(self.upload_message)

    def record_message(self):
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 20
        val = 0

        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            val += (0.006 * RECORD_SECONDS)
            self.recordBar.setValue(val)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        WAVE_OUTPUT_FILENAME = "message.wav"
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

    def play_message(self):
        playsound("message.wav")
        self.playBar.setValue(100)

    def upload_message(self):
        self.uploadBar.setValue(0)
        config = {
            "apiKey": "AIzaSyBuQKF1M7jZp1NqSLuhZGiTVyFOMX4zUxE",
            "authDomain": "mars-8c17e.firebaseapp.com",
            "databaseURL": "https://mars-8c17e.firebaseio.com",
            "storageBucket": "mars-8c17e.appspot.com",
        }

        firebase = pyrebase.initialize_app(config)

        storage = firebase.storage()
        database = firebase.database()
        data = {"Message": "sent"}

        storage.child("message.wav").put("message.wav")
        database.child().push(data)
        self.uploadBar.setValue(100)