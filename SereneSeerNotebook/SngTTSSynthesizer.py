from TTS.api import TTS
import Commons
import os

date = Commons.file_date

# Set the COQUI_STUDIO_TOKEN environment variable
os.environ["COQUI_STUDIO_TOKEN"] = Commons.tts_key

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[24]
# Init TTS
tts = TTS(model_name)

# Example text to be vocalized
text = Commons.all_signs_horoscope

# Set the desired output file path
output_file = f"AllSignsHoroscopeAudio{date}.wav"

# Run TTS and save to the output file
tts.tts_to_file(text= text, file_path=output_file)