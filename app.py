from flask import Flask, render_template, send_from_directory
import os
import pygame

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_audio')
def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load('music/Xtra.mp3')
    pygame.mixer.music.play()
    return 'Audio playing...'

if __name__ == '__main__':
    app.run(debug=True)
