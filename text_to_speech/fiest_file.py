import os
import wave
from urllib.request import urlretrieve
from piper import PiperVoice

# 1. Setup paths
output_dir = "./voices"
os.makedirs(output_dir, exist_ok=True)

model_name = "en_GB-cori-high"
model_path = os.path.join(output_dir, f"{model_name}.onnx")
config_path = os.path.join(output_dir, f"{model_name}.onnx.json")

# Base Hugging Face download URL
base_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium"
# Download URLs for Cori (British Female)
base_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/cori/high/en_GB-cori-high"

# 2. Download files (if not existing)
if not os.path.exists(model_path):
    print("Downloading model...")
    urlretrieve(f"{base_url}.onnx", model_path)

if not os.path.exists(config_path):
    print("Downloading config...")
    urlretrieve(f"{base_url}.onnx.json", config_path)

# 3. Load voice
voice = PiperVoice.load(model_path, config_path=config_path)

# 4. Create synthesis parameters object
# length_scale > 1.0 slows down the speech pace (1.20 = ~20% slower)
# noise_scale < 0.667 smooths out pitch fluctuations (0.50 = smoother delivery)
voice.config.length_scale = 1.25
voice.config.noise_scale = 0.50

# 5. Synthesize directly using synthesize_wav
text = """
some content.

some more content.
more more more .

Example, of using, a comma.
"""
output_wav = "output.wav"

print('generating the file . . .')

with wave.open(output_wav, "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

print(f"Done! The file is here: {output_wav}.")
