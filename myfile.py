import pyaudio
import wave 
from array import array
from struct import pack
import whisper
import os

os.environ['PATH'] += os.pathsep + r'C:\jcffmpeg\bin'

def record(outputFile):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    DURATION = 10

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording....")
    frames = []
    for i in range(0, int(RATE/CHUNK *DURATION)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(outputFile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio(inputFile):
    model = whisper.load_model("base")
    result = model.transcribe(inputFile)
    print(result["text"])
    return result["text"]

# Record the audio
record('output1.wav')

# Transcribe the recorded audio
transcription = transcribe_audio('output1.wav')

# Save the transcription to a text file
with open('transcription.txt', 'w') as f:
    f.write(transcription)



