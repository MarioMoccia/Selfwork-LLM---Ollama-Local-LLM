"""Esercizio 3

Traccia: Crea un prompt che riassuma un articolo di notizie in un singolo paragrafo
di al massimo 255 caratteri.

Obiettivo: Prendere un testo lungo e condensarlo nei punti essenziali.
"""

import ollama

MAX_CHARS = 255
MAX_TENTATIVI = 3

input_text = input("Enter text: ")

messages = [
    {
        "role": "system",
        "content": (
            "Sei un redattore giornalistico. Riassumi l'articolo di notizie che ricevi "
            f"in un singolo paragrafo di circa 200 caratteri, spazi inclusi, e mai più di {MAX_CHARS}. "
            "Mantieni solo i punti essenziali (chi, cosa, dove, quando, perché), "
            "scrivi nella stessa lingua dell'articolo, senza elenchi puntati, "
            "titoli o introduzioni. Rispondi solo con il riassunto."
        ),
    },
    {"role": "user", "content": input_text},
]

# Il modello non conta i caratteri in modo affidabile: se supera il limite
# gli chiedo di accorciare il riassunto, per al massimo MAX_TENTATIVI volte
for tentativo in range(MAX_TENTATIVI):
    response = ollama.chat(model="llama3.2", messages=messages)
    summary = response["message"]["content"].strip()

    if len(summary) <= MAX_CHARS:
        break

    messages.append({"role": "assistant", "content": summary})
    messages.append({
        "role": "user",
        "content": (
            f"Il riassunto è lungo {len(summary)} caratteri, troppi. "
            f"Riscrivilo più breve, in meno di {MAX_CHARS - 40} caratteri."
        ),
    })

print(summary)

if len(summary) > MAX_CHARS:
    print(f"\n[Attenzione] Il riassunto è lungo {len(summary)} caratteri (limite: {MAX_CHARS}).")
