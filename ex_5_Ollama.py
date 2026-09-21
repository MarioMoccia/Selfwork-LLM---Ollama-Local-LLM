"""Esercizio 5

Traccia: Scrivi un prompt che generi domande di comprensione su un breve testo.

Obiettivo: Sviluppare un prompt per creare domande educative basate su un contenuto.
"""

import ollama

input_text = input("Enter text: ")

response = ollama.chat(
    model="llama3.2",
    options={"temperature": 0.2},  # temperatura bassa: domande più aderenti al testo
    messages=[
        {
            "role": "system",
            "content": (
                "Sei un insegnante. Dal breve testo che ricevi genera 3 domande di comprensione "
                "che verifichino se lo studente ha capito il contenuto: due sulle informazioni "
                "esplicite e una che richieda di fare un'inferenza. "
                "Ogni domanda deve riguardare un'informazione diversa e avere la risposta nel testo: "
                "non chiedere dettagli, esempi o elenchi che il testo non riporta e non ripetere "
                "la stessa domanda con parole diverse. Scrivi frasi complete e corrette, nella stessa "
                "lingua del testo. Rispondi solo con un elenco numerato di domande, "
                "senza le risposte."
            ),
        },
        {"role": "user", "content": input_text},
    ],
)

print(response["message"]["content"])
