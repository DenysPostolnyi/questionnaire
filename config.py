import os

import torch
import whisper

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=find_dotenv('.env'))

API_KEY: str = os.getenv('API_KEY')

client = OpenAI(api_key=API_KEY)

AUDIOS_FOLDER = "audios/"

torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium", device=DEVICE)
