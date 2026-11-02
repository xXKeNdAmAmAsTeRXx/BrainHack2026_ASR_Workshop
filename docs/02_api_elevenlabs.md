# 2. Rozwiązania dostępne przez API i strony — 55 min (Mateusz)

> Aktualne materiały: uczestnicy — [02_elevenlabs.pdf](../02_elevenlabs.pdf) (źródło: [handout.md](02_api_elevenlabs/handout.md)), prowadzący — [presentation.md](02_api_elevenlabs/presentation.md). Ten plik to starszy szkic.

**Cel:** hands-on z chmurowym ASR/TTS na przykładzie **ElevenLabs** + krytyczne spojrzenie na dane.

## Program
1. **Transkrypcja (STT)** przez www — wgranie nagrania własnego głosu (z wymagań wstępnych)
2. **Transkrypcja + diaryzacja** — kto mówi, kiedy; eksporty
3. **Text-to-speech** — generowanie mowy; **voice cloning** na własnym nagraniu (~1 min)
4. **Dostęp przez API — przykład kodu** (Python `requests`, key z dashboardu)

## Przykład kodu (szkic)
```python
import requests

API_KEY = "..."  # ElevenLabs dashboard

# Speech-to-text
files = {"file": open("moj_glos.wav", "rb")}
headers = {"xi-api-key": API_KEY}
r = requests.post("https://api.elevenlabs.io/v1/speech-to-text",
                  headers=headers, files=files, data={"model_id": "scribe_v2"})
print(r.json())

# Text-to-speech
r = requests.post(
    "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    headers=headers,
    json={"text": "Cześć, to jest test.", "model_id": "eleven_multilingual_v2"})
open("wynik.mp3", "wb").write(r.content)
```
*(aktualne endpointy: https://elevenlabs.io/docs/api-reference)*

## Prywatność: sprawdź, jak przechowywane są dane
- Gdzie serwery / przetwarzanie (UE vs USA)?
- Retencja: czy audio/text zostaje po transkrypcji? Opt-out z treningu modeli?
- **Zero data retention** na Enterprise — co to znaczy dla danych medycznych?
- Ćwiczenie: przeczytać https://elevenlabs.io/privacy i znaleźć odpowiedzi

## Fireflies (notatki ze spotkań)
- https://fireflies.ai/pricing — bot na spotkania: transkrypcja + diaryzacja + AI streszczenia
- Porównać plany (free vs paid) i model danych (bot wchodzi na spotkanie = czy każdy wie?)

## Wymagania
- konto ElevenLabs (z wymagań wstępnych)
- nagranie własnego głosu (~1 min)
- Python 3.10+ / Colab, `pip install requests`
