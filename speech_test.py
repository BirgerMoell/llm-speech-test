import openai
import os
from dotenv import load_dotenv
from tts import synthesize_speech

load_dotenv()

openai.api_key = os.getenv("OPEN_API_NEW_KEY")

def get_response_from_chat_gpt_story_bot(text):
    print("getting a response from chat gpt for the text", text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du är en AI bot som skriver spännande och engagerande berättelser. Dina berättelser är välskrivna och intressanta att lyssan på."},
            {"role": "user", "content": text}
        ]
    )

    text = response['choices'][0]['message']['content']
    return text

# print(get_response_from_chat_gpt("I am feeling anxious."))
story = get_response_from_chat_gpt_story_bot("Skriv en berättelse om en katt som är rädd för hundar.")
print(story)

synthesize_speech(story, language="sv")