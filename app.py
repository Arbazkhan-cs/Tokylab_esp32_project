import time
from llm import invoke_llm
from text_to_speech import text_to_speech
from speech_to_text import speech_to_text
from play_audio_final import play_audio
from record_audio_final import record_audio
from config import credentials

# Main application logic
def main():
    groq_api_key = credentials.get("GROQ_API_KEY")

    try:
        print("Recording audio...")
        record_audio("recorded_audio.raw")
        print("Audio recording completed.\n")
        
    except Exception as e:
        print(f"Error during audio recording: {e}")
        return

    try:
        print("Processing audio...")
        prompt = speech_to_text("recorded_audio.raw")
        print(f"Audio processing completed: {prompt}\n")
    except Exception as e:
        print(f"Error during audio processing: {e}")
        return

    try:
        print("Generating response...")
        response = invoke_llm(prompt, groq_api_key)
        print(f"Response generation completed: {response}\n")

    except Exception as e:
        print(f"Error during response generation: {e}")
        return

    try:
        print("Converting text to speech...")
        if text_to_speech(response, "synthesized_audio.wav"):
            print("Text-to-speech conversion completed.\n")
        else:
            print("Error during text-to-speech conversion.\n")
            return
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")
        return

    try:
        print("Playing synthesized audio...")
        play_audio("synthesized_audio.wav")
        print("Audio playback completed.\n")
    except Exception as e:
        print(f"Error during audio playback: {e}")

if __name__ == "__main__":
    main()