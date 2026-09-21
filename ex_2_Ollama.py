"""Esercizio 2

Traccia: Crea un prompt che estragga i dettagli chiave (nome, età, professione)
da un testo descrittivo su una persona.

Obiettivo: Estrarre informazioni strutturate da un testo libero.
"""

import ollama

input_text = input("Enter text: ")

response = ollama.chat(
    model="llama3.2",
    format="json",  # forza l'output a essere un JSON valido
    messages=[
        {
            "role": "system",
            "content": (
                "Estrai dal testo che ricevi i dettagli chiave di una persona: "
                "nome, età e professione. "
                "Rispondi solo con un oggetto JSON valido con esattamente queste chiavi: "
                '"nome", "età", "professione". '
                "L'età deve essere un numero intero. "
                "Se un'informazione non è presente nel testo usa null, senza inventare nulla. "
                "Non aggiungere commenti."
            ),
        },
        {"role": "user", "content": input_text},
    ],
)

print(response["message"]["content"])
