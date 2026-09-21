"""Esercizio 4

Traccia: Trasforma un set di dati strutturati (come un dizionario Python)
in una descrizione testuale completa.

Obiettivo: Convertire dati strutturati in una descrizione leggibile.
"""

import json
import ollama

data = {"name": "Giovanni", "age": 30, "city": "Roma", "profession": "Ingegnere"}

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": (
                "Trasforma i dati strutturati che ricevi (in formato JSON) in una descrizione "
                "testuale completa e scorrevole, in italiano, in terza persona. "
                "Usa tutti i campi presenti e nessuna informazione che non sia nei dati: "
                "non aggiungere commenti, valutazioni, deduzioni o dettagli inventati. "
                "Scrivi un breve paragrafo, non un elenco. Rispondi solo con la descrizione."
            ),
        },
        {"role": "user", "content": json.dumps(data, ensure_ascii=False)},
    ],
)

print(response["message"]["content"])
