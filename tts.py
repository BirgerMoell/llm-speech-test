import torch
import soundfile as sf
import uuid
import subprocess
import time

def synthesize_speech(text, language="en"):
    # get time for the tts system
    start_time = time.time()
    # strip space from text
    stripped_text = text.strip()
    # make stripped text 5 chars long
    stripped_text = stripped_text[:5]
    file_path = "speech/" + stripped_text +str(uuid.uuid4()) + ".mp3"

    if language == "en":
        subprocess.call(["tts", "--text", text, "--model_name", "tts_models/en/vctk/vits", "--speaker_idx", "p225", "--out_path", file_path ])
        print(file_path)
        print("tts took", time.time() - start_time, "seconds")
        return file_path
    elif language == "sv":
        subprocess.call(["tts", "--text", text, "--model_name", "tts_models/sv/cv/vits", "--out_path", file_path ])
        print(file_path)
        print("tts took", time.time() - start_time, "seconds")
        return file_path

# synthesize_speech("Jag gillar potatis", language="sv")