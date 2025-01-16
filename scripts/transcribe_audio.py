import os
from utils import load_audio, preprocess_audio
from phonetic_model import transcribe_phonetically

def transcribe_audio_files(input_dir, output_dir):
    """
    Transcribes all audio files in the input directory and saves the phonetic transcriptions.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):  # Assuming audio files are in .wav format
            audio_path = os.path.join(input_dir, filename)
            audio = load_audio(audio_path)
            processed_audio = preprocess_audio(audio)  # Optional: Preprocess audio (e.g., noise reduction)
            phonetic_transcription = transcribe_phonetically(processed_audio)
            
            # Save transcription to output directory
            output_path = os.path.join(output_dir, filename.replace(".wav", ".txt"))
            with open(output_path, "w") as f:
                f.write(phonetic_transcription)

if __name__ == "__main__":
    input_dir = "data/raw_audio"
    output_dir = "data/phonetic_transcriptions"
    transcribe_audio_files(input_dir, output_dir)
