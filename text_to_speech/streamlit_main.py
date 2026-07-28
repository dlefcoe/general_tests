"""
streamlit run "text_to_speech/streamlit_main.py"
"""

import os

import streamlit as st
import tts_helper
from piper import PiperVoice

OUTPUT_WAV = "text_to_speech/output_stream.wav"


@st.cache_resource
def setup_piper_voice(
    slowdown_factor=1.25, smoothness_factor=0.50
) -> None | PiperVoice:
    """Loads and caches the Piper TTS voice model."""
    model_path, config_path = tts_helper.setup_paths()
    base_url = tts_helper.base_url_select()

    files_exist = tts_helper.download_files(base_url, model_path, config_path)
    if not files_exist:
        return None

    return tts_helper.prepare_voice(
        model_path, config_path, slowdown_factor, smoothness_factor
    )


def handle_synthesis(text: str, voice: PiperVoice | None) -> None:
    """Validates inputs and runs text-to-speech synthesis."""
    if not text.strip():
        st.warning("Please enter some text first.")
        return

    if voice is None:
        st.error("The voice was not set up properly.")
        return

    with st.spinner("Synthesizing speech..."):
        tts_helper.synthesize_wav(voice, text, output_wav=OUTPUT_WAV)

    if not os.path.exists(OUTPUT_WAV):
        st.error("Audio generated, but output file was not found.")
        return

    st.success("Audio generated!")


def play_audio(file_path: str) -> None:
    """Reads a WAV file and renders the player and download button."""
    if not os.path.exists(file_path):
        st.error(f"Audio file '{file_path}' was not found.")
        return

    with open(file_path, "rb") as f:
        audio_bytes = f.read()

    st.success("Audio generated!")
    st.audio(audio_bytes, format="audio/wav")
    st.download_button(
        label="Download WAV Audio",
        data=audio_bytes,
        file_name="speech.wav",
        mime="audio/wav",
    )

    # delete the output file
    os.remove(file_path)


def main():
    st.title("Piper TTS Speech Generator")

    text_input = st.text_area("Enter Text:", "Hello... take a deep breath, and relax.")

    # TODO: set up speed sliders.
    # slowdown factor 0.5 to 2.0
    slowdown_factor = st.slider(
        label="slowdown factor:",
        min_value=0.5,
        max_value=2.0,
        value=1.2,  # Default starting position
        step=0.1,
    )
    # smoothness factor 0.25 to 1.00
    smoothness_factor = st.slider(
        label="smoothness:",
        min_value=0.2,
        max_value=1.0,
        value=0.6,  # Default starting position
        step=0.1,
    )

    voice = setup_piper_voice(slowdown_factor=slowdown_factor, smoothness_factor=smoothness_factor)

    if st.button("Generate Speech"):
        handle_synthesis(text_input, voice)

    if st.button("Read Generated Audio"):
        play_audio(OUTPUT_WAV)


if __name__ == "__main__":
    main()
