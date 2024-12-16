import torch
from transformers import pipeline
import librosa
import io
import base64
import boto3


#converts audio bytes to array
def convert_bytes_to_array(audio_bytes):
    audio_bytes = io.BytesIO(audio_bytes)
    audio, sr = librosa.load(audio_bytes)
    # print(sr)
    return audio


#pipeline for audio output
def transcribe_audio(audio_bytes):

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    # print("Device",device)

    pipe = pipeline(
        task = "automatic-speech-recognition",
        model="openai/whisper-small",
        chunk_length_s=30,
        device=device,
    )
    audio_array = convert_bytes_to_array(audio_bytes)
    prediction = pipe(audio_array, batch_size=1)["text"]
    return prediction


