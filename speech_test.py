import openai
import os
from dotenv import load_dotenv
from tts import synthesize_speech
from azure_tts import azure_tts

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


def get_response_from_chat_gpt_evaluate_bot(text, summary):
    #print("getting a response from chat gpt for the text", text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du är en AI bot som utvärderar sammanfattningar av text. Det här är texten som du ska sammanfatta:" + text},
            {"role": "user", "content": "Sammanfattning: " + summary + " Svara enbart med en siffra 0-10:"}
        ]
    )

    text = response['choices'][0]['message']['content']
    return text


story = get_response_from_chat_gpt_story_bot("Skriv en berättelse på 50 ord")
print(story)

#score = get_response_from_chat_gpt_evaluate_bot(story, "En historia om en modig människa")

#print("the score is", score)
# synthesize_speech(story, language="sv")
output_filepath = azure_tts(story)