
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")
URL = "https://pesmed.pl/lekarz"

def ask_chat_for_specialist(symptoms):
    prompt = (
        "Na podstawie podanych objawów określ, do jakiego lekarza specjalisty "
        "powinien udać się pacjent. Podaj tylko nazwę specjalizacji (np. dermatolog, neurolog), "
        "bez dodatkowego komentarza.\n\n"
        f"Objawy: {symptoms}\nSpecjalista:"
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"Jesteś asystentem medycznym, który na podstawie objawów wybiera specjalistę."},
            {"role":"user","content":prompt}
        ],
        max_tokens=50,
    )

    reply = response.choices[0].message.content
    return reply


