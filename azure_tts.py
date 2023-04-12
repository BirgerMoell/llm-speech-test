import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

def azure_tts(text: str) -> str:
    # Replace with your own API key and endpoint from the Azure portal
    speech_key = os.getenv("AZURE_SPEECH_KEY")
    service_region = os.getenv("AZURE_SPEECH_REGION")

    # Create a Speech configuration object
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Set the voice for the synthesizer
    speech_config.speech_synthesis_voice_name = "sv-SE-SofieNeural"

    # Create a Text-to-Speech client
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Synthesize the text to speech
    result = speech_synthesizer.speak_text_async(text).get()

    # Check if the synthesis was successful and save the output to a file
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        output_filepath = "output.wav"
        stripped_text = text.strip()
        # make stripped text 5 chars long
        stripped_text = stripped_text[:5]
        output_filepath = "speech/" + stripped_text +str(uuid.uuid4()) + ".wav"

        with open(output_filepath, "wb") as audio_file:
            audio_file.write(result.audio_data)
        return output_filepath
    else:
        print(f"Speech synthesis failed with status: {result.reason}.")
        return None

# # Usage example
# text = "Hej, det här är en exempeltext."
# output_filepath = azure_tts(text)

# if output_filepath:
#     print(f"Audio saved to {output_filepath}.")
# else:
#     print("Failed to synthesize speech.")