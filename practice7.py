# Text-to-Speech Inference Script using Hugging Face VITS Model
# Author: [Your Name]
# Date: [Insert Date]
# Description: Clone a pre-trained TTS model from Hugging Face, synthesize speech from text, and save/play audio.

# Step 1: Install required packages (run this in terminal if not already installed)
# pip install transformers torch soundfile IPython

# Step 2: Import necessary libraries
from transformers import VitsModel, AutoTokenizer
import torch
import soundfile as sf
from IPython.display import Audio  # Optional for Jupyter playback
import simpleaudio as sa


# Step 3: Load pre-trained TTS model and tokenizer from Hugging Face
# You can replace "facebook/mms-tts-vie" with another compatible TTS model
#facebook/mms-tts-vie
#suno/bark
#myshell-ai/OpenVoice
#microsoft/speecht5
#coqui/tts
#espnet/kan-bayashi-jsut-tts
#uberduck-ai models

model_name = "facebook/mms-tts-vie"
model = VitsModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Step 4: Prepare input text
text = "Xin chào anh em đến với bài tập của khoá AI Application Engineer, mình là Truyền đây"
print("Text input:",text)
# Step 5: Tokenize the input text
inputs = tokenizer(text, return_tensors="pt")

# Step 6: Perform inference to generate waveform
with torch.no_grad():
    output = model(**inputs).waveform

# Step 7: Save the generated audio to a .wav file
output_path = "output.wav"
#audio = AudioSegment.from_file("file.m4a", format="m4a")
#audio.export("output.wav", format="wav")  # Chuyển sang WAV để dùng với soundfile

waveform = output.squeeze().numpy().astype("float32")
# Optional: Play audio in Jupyter Notebook
#Audio(output.numpy(), rate=model.config.sampling_rate) 

#write file audio
sf.write(output_path, waveform, samplerate=model.config.sampling_rate)

print(f"✅ Audio saved to {output_path}")

#Try play it
wave_obj = sa.WaveObject.from_wave_file(output_path)
play_obj = wave_obj.play()
play_obj.wait_done()  # Chờ phát xong


# Step 8: Notes
# - You can change the input text to test other sentences.
# - For deployment, consider using Hugging Face Spaces with Gradio or Streamlit.


#Run: py practice7.py