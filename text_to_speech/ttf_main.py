import os
import wave
from urllib.request import urlretrieve

from piper import PiperVoice


def setup_paths():
    """function to setup paths for model and config files"""
    output_dir = "./voices"
    os.makedirs(output_dir, exist_ok=True)

    model_name = "en_GB-cori-high"
    model_path = os.path.join(output_dir, f"{model_name}.onnx")
    config_path = os.path.join(output_dir, f"{model_name}.onnx.json")

    return model_path, config_path


def base_url_select(gender="female"):
    """function to return the base URL for downloading model and config files"""

    print("selecting the base URL for downloading model and config files...")

    if gender == "male":
        # Base Hugging Face download URL
        base_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium"

    elif gender == "female":
        # Download URLs for Cori (British Female)
        base_url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/cori/high/en_GB-cori-high"

    else:
        raise ValueError("Invalid gender specified. Choose 'male' or 'female'.")

    return base_url


def download_files(base_url, model_path, config_path):
    """function to download model and config files if they do not exist"""
    if not os.path.exists(model_path):
        print("Downloading model...")
        urlretrieve(f"{base_url}.onnx", model_path)
    else:
        print("Model already exists. Skipping download.")

    if not os.path.exists(config_path):
        print("Downloading config...")
        urlretrieve(f"{base_url}.onnx.json", config_path)
    else:
        print("Config already exists. Skipping download.")

    return True


def prepare_voice(
    model_path, config_path, slowdown_factor=1.25, smoothness_factor=0.50
):
    """function to prepare the voice for synthesis"""
    voice = PiperVoice.load(model_path, config_path=config_path)

    # Set synthesis parameters
    voice.config.length_scale = (
        slowdown_factor  # Slows down speech pace (1.20 = ~20% slower)
    )
    voice.config.noise_scale = (
        smoothness_factor  # < 0.667 Smooths out pitch fluctuations
    )

    return voice


def synthesize_wav(voice, text="some placeholder text", output_wav= "text_to_speech/output.wav"):
    """function to synthesize text to wav file"""

    print("generating the file . . .")
    with wave.open(output_wav, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    print(f"Done! The file is here: {output_wav}.")
    return True

def main():
    # 1. Setup paths for model and config files
    model_path, config_path = setup_paths()

    base_url = base_url_select()

    # 2. Download files (if not existing)
    files_exist = download_files(base_url, model_path, config_path)
    if files_exist:
        print("Model and config files are ready.")
    else:
        print("Failed to download model and config files.")
        return

    # 3. Load voice
    print("Loading voice...")
    voice = prepare_voice(model_path, config_path, slowdown_factor=1.25, smoothness_factor=0.50)

    # 5. Synthesize directly using synthesize_wav
    text = """
    the code works 3
    """
    # output_wav = "text_to_speech/output.wav"

    synthesize_wav(voice, text)

# main guard idiom
if __name__ == "__main__":
    main()
