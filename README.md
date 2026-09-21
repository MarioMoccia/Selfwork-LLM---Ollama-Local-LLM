# Selfwork LLM - Ollama Local LLM

Gli stessi cinque esercizi di prompt engineering del selfwork "OpenAI Chat Completion", ma con un LLM
che gira in locale tramite [Ollama](https://ollama.com) e il metodo `ollama.chat` della libreria Python.
Nessuna chiave API e nessun costo: il modello gira sul tuo computer.

| File | Esercizio |
|---|---|
| `ex_1_Ollama.py` | Traduzione italiano ⇄ inglese di una descrizione di prodotto |
| `ex_2_Ollama.py` | Estrazione di nome, età e professione da un testo (output JSON) |
| `ex_3_Ollama.py` | Riassunto di un articolo in massimo 255 caratteri |
| `ex_4_Ollama.py` | Da dizionario Python a descrizione testuale |
| `ex_5_Ollama.py` | Generazione di domande di comprensione su un testo |

## Setup

1. Installa Ollama da <https://ollama.com/download> e avvialo.
2. Scarica il modello usato dagli esercizi:
   ```bash
   ollama pull llama3.2
   ```
3. Crea l'ambiente Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Uso

```bash
python ex_1_Ollama.py
```

Gli esercizi 1, 2, 3 e 5 chiedono un testo da terminale; l'esercizio 4 usa un dizionario definito nel codice.
Per usare un altro modello basta cambiare il parametro `model` nella chiamata a `ollama.chat`.

## Note sul modello

`llama3.2` è un modello piccolo (3B parametri) che gira anche su un portatile, ma ha dei limiti:

- **Esercizio 1:** decide male la direzione della traduzione se gli si chiede di rilevare la lingua e tradurre nella stessa richiesta. Per questo il codice usa due chiamate a `ollama.chat`: la prima rileva la lingua, la seconda traduce verso una lingua indicata in modo esplicito. La traduzione verso l'italiano può contenere errori di lessico.
- **Esercizio 3:** non conta i caratteri in modo affidabile. Se il riassunto supera i 255 caratteri, lo script chiede al modello di accorciarlo (fino a 3 tentativi).
- **Esercizio 5:** con temperatura bassa e poche domande le domande restano aderenti al testo.

Per risultati migliori si può provare un modello più grande, ad esempio `ollama pull llama3.1:8b` e poi `model="llama3.1:8b"`.
