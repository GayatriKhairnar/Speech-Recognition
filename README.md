# Speech-Recognition
This project demonstrates a simple speech-to-text recognition system using PyAudio for recording audio and OpenAI's Whisper model for transcribing the recorded audio. The following steps are carried out in the code:

### Audio Recording:

Utilizes the pyaudio library to capture audio input from the microphone.
Records 10 seconds of audio with a sample rate of 44.1 kHz, 2 channels, and 16-bit format.
Saves the recorded audio to a file named output1.wav.

### Audio Transcription:

Loads the pre-trained Whisper model.
Transcribes the recorded audio file (output1.wav) to text.
Prints the transcription to the console.

### Save Transcription:

Writes the transcribed text to a file named transcription.txt.
How to Use

### Ensure you have the required dependencies installed:

- pyaudio
- wave
- whisper
  


