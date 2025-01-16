
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from utils import preprocess_audio
from phonetic_model import transcribe_phonetically
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def record_audio(duration=5, sample_rate=16000):
    """
    Records audio from the microphone.
    """
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    return audio.flatten()

def real_time_typing():
    """
    Real-time voice typing with user interaction.
    """
    # Load fine-tuned GPT-2 model
    tokenizer = GPT2Tokenizer.from_pretrained("models/gpt2_finetuned")
    model = GPT2LMHeadModel.from_pretrained("models/gpt2_finetuned")

    while True:
        # Record audio
        audio = record_audio()
        processed_audio = preprocess_audio(audio)
        phonetic_transcription = transcribe_phonetically(processed_audio)

        # Generate text using fine-tuned GPT-2
        input_ids = tokenizer.encode(phonetic_transcription, return_tensors="pt")
        output = model.generate(input_ids, max_length=50)
        text = tokenizer.decode(output[0], skip_special_tokens=True)

        # Display transcription and allow user interaction
        print(f"Transcription: {text}")
        user_input = input("Confirm (c), Flag (f), or Correct (r): ").strip().lower()
        if user_input == "c":
            print("Transcription confirmed.")
        elif user_input == "f":
            print("Transcription flagged for review.")
        elif user_input == "r":
            corrected_text = input("Enter corrected text: ")
            print(f"Corrected text saved: {corrected_text}")

if __name__ == "__main__":
    real_time_typing()
