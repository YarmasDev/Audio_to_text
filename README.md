# Audio to Text Transcription and Translation

This project utilizes Streamlit and Groq to provide an audio transcription and translation service. Users can either upload an audio file or record their voice directly through the web application.

## Features

- Upload audio files in formats: m4a, mp3, wav
- Record audio directly in the browser
- Automatic transcription of audio to text
- Translation of transcribed text

## Getting Started

To run this project locally, ensure you have the required packages installed. You can do this by using the `requirements.txt` file provided in the repository.

### Prerequisites

- Python 3.7 or higher
- Streamlit
- streamlit-mic-recorder
- Groq

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd audio_to_text
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run audio_to_text.py
   ```

## Usage

1. Navigate to the app in your browser after running the above command. By default, it will be available at `http://localhost:8501`.
2. You can either:
   - Upload an audio file using the file uploader.
   - Or, click the "Start recording" button to record your voice directly.
3. Once the audio is processed, the transcription and translation will be displayed on the screen.

## Live Demo

You can also try the live version of the application here: https://audiototext-abv9xytvl24cayxllpbyp5.streamlit.app/

