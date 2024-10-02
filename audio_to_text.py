import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
from io import BytesIO
import time
from groq._base_client import APIConnectionError

# Initialize the Groq client using secrets
api_key = st.secrets["API_KEY"]["key"]
client = Groq(api_key=api_key)

def chat():
    st.title("Audio Transcription and Translation")
    st.write("Let AI transcribe and translate your audio in seconds")

    # Section for uploading audio files
    uploaded_file = st.file_uploader("Upload an audio file", type=["m4a", "mp3", "wav"])
    
    # Section for recording audio
    st.subheader("Or record your voice:")
    mic_output = mic_recorder(
        start_prompt="Start recording",
        stop_prompt="Stop recording",
        just_once=False,
        key="audio_recorder"
    )

    # Check if an audio file has been uploaded
    if uploaded_file is not None:
        with st.spinner("Processing uploaded audio..."):
            try:
                transcription = client.audio.transcriptions.create(
                    file=(uploaded_file.name, uploaded_file.read()),  # The uploaded audio file
                    model="whisper-large-v3",
                    response_format="json",
                    temperature=0.0
                )
                
                st.subheader("Transcription from uploaded file:")
                st.write(transcription.text)

                uploaded_file.seek(0)  # Reset the file pointer for translation
                translation = client.audio.translations.create(
                    file=(uploaded_file.name, uploaded_file.read()),
                    model="whisper-large-v3",
                    response_format="json",
                    temperature=0.1
                )

                st.subheader("Translation from uploaded file:")
                st.write(translation.text)
            
            except APIConnectionError:
                st.error("Error connecting to the API. Please try again later.")

    # Check if audio has been recorded
    if mic_output and "bytes" in mic_output:
        audio_bytes = mic_output['bytes']
        st.audio(audio_bytes, format="audio/wav")  # Play the recorded audio

        with st.spinner("Processing recorded audio..."):
            audio_buffer = BytesIO(audio_bytes)  # Convert audio to BytesIO

            try:
                transcription = client.audio.transcriptions.create(
                    file=("recorded_audio.wav", audio_buffer),  # Use BytesIO for the recorded audio
                    model="whisper-large-v3",
                    response_format="json",
                    temperature=0.0
                )
                
                st.subheader("Transcription from recorded audio:")
                st.write(transcription.text)

                translation = client.audio.translations.create(
                    file=("recorded_audio.wav", audio_buffer),
                    model="whisper-large-v3",
                    response_format="json",
                    temperature=0.1
                )

                st.subheader("Translation from recorded audio:")
                st.write(translation.text)
            
            except APIConnectionError:
                st.error("Error connecting to the API. Retrying...")
                time.sleep(2)
                
                try:
                    transcription = client.audio.transcriptions.create(
                        file=("recorded_audio.wav", audio_buffer),
                        model="whisper-large-v3",
                        response_format="json",
                        temperature=0.0
                    )
                    st.subheader("Transcription from recorded audio (Retry):")
                    st.write(transcription.text)

                    translation = client.audio.translations.create(
                        file=("recorded_audio.wav", audio_buffer),
                        model="whisper-large-v3",
                        response_format="json",
                        temperature=0.1
                    )
                    st.subheader("Translation from recorded audio (Retry):")
                    st.write(translation.text)

                except APIConnectionError:
                    st.error("Error connecting while retrying transcription and translation.")

if __name__ == "__main__":
    chat()
