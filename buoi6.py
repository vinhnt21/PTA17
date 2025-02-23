from PyQt6 import uic
from PyQt6.QtWidgets import *
import pygame


class Buoi6(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi6.ui", self)

        self.pushButton.clicked.connect(self.play_music)
        self.pushButton_2.clicked.connect(self.stop_music)

        # Music
        pygame.init()
        pygame.mixer.init()

    def play_music(self):
        music_file = "buoi6.mp3"
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()


app = QApplication([])
window = Buoi6()
window.show()
app.exec()
