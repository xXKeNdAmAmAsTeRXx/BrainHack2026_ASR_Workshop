# ElevenLabs — materiał dla uczestników

**Warsztaty BrainHack 2026 — Rozpoznawanie i generowanie mowy**  
Moduł 2 (55 min) · Prowadzący: Franciszek Kubala, Mateusz Poszelężny — KN AIMed AGH

> W tej części pracujemy głównie przez stronę ElevenLabs. Wgrasz własne nagranie, sprawdzisz transkrypcję, zobaczysz podział rozmowy na mówców i wygenerujesz mowę z tekstu. Poznasz też klonowanie głosu i sposób uzyskania dostępu przez API.

---

## 1. Co będziemy robić?

- **Speech-to-text (STT):** nagranie → tekst. W ElevenLabs służy do tego model **Scribe**.
- **Diaryzacja:** podział rozmowy na wypowiedzi poszczególnych mówców.
- **Text-to-speech (TTS):** tekst → syntetyczna mowa wybranym głosem.
- **Voice cloning:** utworzenie głosu na podstawie próbki, a następnie użycie go do czytania nowego tekstu.
- **API:** dostęp do usługi z własnego programu, zamiast ręcznego klikania na stronie.

**Przykład:** nagrywasz rozmowę → otrzymujesz tekst z oznaczeniami mówców → sprawdzasz błędy → zapisujesz wynik.

---

## 2. Co przygotować przed ćwiczeniami?

- Konto na [ElevenLabs](https://elevenlabs.io), przeglądarkę, internet i słuchawki.
- Około **1 minuty własnej, neutralnej wypowiedzi** w pliku WAV lub MP3. Mów wyraźnie, w cichym miejscu, bez muzyki i innych osób w tle.

**Konto i koszty:** plan Free obejmuje STT i TTS w dostępnych limitach. **Instant Voice Cloning jest dostępne od planu Starter**, a Professional Voice Cloning od Creator. Aktualna dostępność: [cennik ElevenLabs](https://elevenlabs.io/pricing).

---

## 3. Ćwiczenie A — transkrypcja własnego głosu (STT)

### Krok po kroku

1. Zaloguj się do ElevenLabs i otwórz **Mowa na text**.
2. Kliknij **Transkrybuj pliki** i wybierz własny plik.
3. Ustaw język polski albo pozostaw **Wykryj**, czyli automatyczne wykrywanie języka.
4. Opcjonalne **Oznacz wydarzenia audio** oznacza dźwięki takie jak śmiech.
5. Kliknij **Prześlij pliki** i poczekaj na wynik. Następnie otwórz transkrypcję, wybierając nazwę pliku.
6. Kliknij wybrane słowo, aby odsłuchać odpowiadający mu fragment. Popraw zauważone błędy w edytorze.

### Co sprawdzić?

Odsłuchaj 15–20 sekund i porównaj dźwięk z tekstem. Zwróć uwagę na nazwy własne, liczby i przeczenia: pominięte „nie” może odwrócić sens wypowiedzi. Sprawdź też, czy model nie pominął fragmentu albo nie dopisał słów.

---

## 4. Ćwiczenie B — transkrypcja i diarizacja rozmowy

**Diarizacja odpowiada na pytanie „który mówca mówi w danym momencie?”.** Otrzymujesz etykiety, np. `Speaker 1` i `Speaker 2`. Same etykiety nie podają imion ani nie potwierdzają tożsamości osób.

### Krok po kroku

1. W **Speech to Text** wgraj plik z rozmową tak jak w ćwiczeniu A. Na stronie internetowej podział na mówców jest już uwzględniony w wyniku; W API włącza się go parametrem `diarize`.
2. Otwórz wynik i odszukaj oznaczenia mówców.
3. Odsłuchaj momenty zmiany osoby. Sprawdź, czy wypowiedź trafiła do właściwego mówcy i czy ta sama osoba zachowuje jedną etykietę.
4. W sekcji **Speakers**, przyciskiem edycji, możesz zmienić nazwy na „Osoba A” i „Osoba B”. To Twoja adnotacja po odsłuchu.

Opis funkcji: [diarizacja i nazwy mówców w interfejsie](https://elevenlabs.io/docs/eleven-creative/playground/speech-to-text), [parametry diarizacji w API](https://elevenlabs.io/docs/api-reference/speech-to-text/convert).

**Efekt ćwiczenia:** sprawdzisz co najmniej dwie zmiany mówcy. Zapisz osobno błędy tekstu i błędy przypisania osoby — poprawne słowa mogą być przypisane niewłaściwemu mówcy. Nakładanie się głosów i hałas utrudniają oba zadania.

---

## 5. Zapis transkrypcji i oznaczeń mówców

W otwartej transkrypcji kliknij **Exportuj** i wybierz format odpowiedni do zadania:

- **TXT:** tekst do czytania i dalszej pracy.
- **SRT lub VTT:** napisy z czasem wyświetlania.
- **JSON, jeśli jest dostępny w danym eksporcie:** dane do programu, np. tekst, czas i identyfikator mówcy. Taki wynik otrzymasz też przez API.

Zapisz wynik jako `diaryzacja`. **Otwórz pobrany plik i sprawdź, czy zawiera potrzebne czasy i etykiety mówców**

---

## 6. Ćwiczenie C — generowanie mowy (TTS)

1. Otwórz **Text to Speech**.
2. Wklej krótki tekst z przykładu poniżej.
3. Wybierz dostępny na Twoim koncie głos obsługujący język polski, np. **Marcin - Polish Narrator**.
4. Kliknij **Wygeneruj mowę**, odsłuchaj wynik i pobierz audio.

> „Witaj na warsztatach BrainHack. Dzisiaj sprawdzimy, jak komputer rozpoznaje mowę i czyta napisany tekst. Zrób krótką przerwę, a potem porównaj oba nagrania.”

**Efekt ćwiczenia:** zapiszesz krótkie audio i wskażesz, co w jego wymowie lub tempie odpowiada Twojemu zastosowaniu, np. nagraniu instrukcji dla uczestników badania.

---

## 7. Pokaz — klonowanie własnego głosu

**Voice cloning** tworzy głos, którym następnie można wygenerować wypowiedź na podstawie nowego tekstu. Do krótkiego pokazu wykorzystujemy **Instant Voice Cloning**, z próbką około 1–2 minut czystej mowy jednej osoby. Professional Voice Cloning wymaga większej ilości materiału i dodatkowego procesu przygotowania;

---

## 8. Jak uzyskać dostęp przez API?

**Klucz API** uprawnia program do korzystania z Twojego konta i jego limitów, dzięki czemu możesz automatyzować procesy związane z przetwarzaniem mowy.

### Utworzenie klucza na stronie

1. W panelu konta otwórz **Deweloperzy → Klucze API**.
2. Wybierz utworzenie klucza i nazwij go, np. `brainhack-warsztat`.
3. Pozostaw ograniczenia klucza i włącz tylko potrzebne uprawnienia: **Speech to Text** oraz **Text to Speech**.
4. Skopiuj klucz.
5. Po ćwiczeniach możesz usunąć klucz, jeśli nie będzie już potrzebny.

| **Ważne** | - nigdy nie pokazuj, ani nie udostępniaj publicznie swojego klucza API innym osobą.  

### Co program wysyła i otrzymuje?

- **STT:** wysyła plik i wybór modelu do `POST /v1/speech-to-text`. Otrzymuje **JSON**, czyli dane zawierające m.in. tekst, czasy słów i — po włączeniu diarizacji — identyfikatory mówców.
- **TTS:** wysyła tekst, identyfikator głosu (`voice_id`) i model do `POST /v1/text-to-speech/{voice_id}`. Otrzymuje **plik audio**.

**Efekt tej części:** potrafisz znaleźć miejsce tworzenia klucza i zastosować go w przykładowym programie. 
---

## 9. Prywatność — co sprawdzić na koncie?

Przez stronę i przez API wysyłasz dane do usługi chmurowej. W grę wchodzą nagrania, teksty, transkrypcje i próbki głosu.

**Ćwiczenie:** wejdź w menu profilu → **Terms and privacy → Data use**. Znajdź opcję **Improve the models for everyone**. Jeśli nie chcesz udostępniać nowych danych do ulepszania modeli, wyłącz ją i zapisz wybór przez **Update your choice**. Według instrukcji producenta wybór dotyczy nowych danych; nie oznacza automatycznego usunięcia wcześniejszych plików.

Przed użyciem narzędzia poza warsztatem ustal:

- **Cel i zgodę:** czy osoby wiedzą o nagraniu, wysyłce do dostawcy i ewentualnym klonowaniu głosu?
- **Dostęp:** kto zobaczy pliki i wyniki?
- **Przechowywanie:** jak długo dane pozostają u dostawcy i jak je usunąć?
- **Miejsce przetwarzania:** jaki region i warunki dotyczą konkretnego konta lub umowy?

Wyłączenie treningu i usunięcie pliku to osobne działania. Nie zakładaj też zerowej retencji na zwykłym koncie, tzn. pliki, które udostępniasz nie są automatycznie usuwane. 

W module 4 porównamy to z Whisperem uruchamianym samodzielnie. **Colab również jest chmurą — Google.** Uruchomienie modelu na własnym komputerze i uruchomienie go w Colabie to różne miejsca przetwarzania danych.

---

## 10. Słownik pojęć

- **Transkrypcja:** tekstowa wersja nagrania.
- **Diarizacja:** przypisanie fragmentów nagrania do poszczególnych mówców.
- **Znacznik czasu:** informacja, kiedy wystąpiło słowo lub fragment.
- **Voice cloning:** utworzenie głosu na podstawie nagrania do generowania nowych wypowiedzi.
- **API:** sposób komunikacji programu z usługą.
- **Klucz API:** poufny klucz dostępu powiązany z kontem i uprawnieniami.
- **`voice_id`:** identyfikator wybranego głosu.
- **`model_id`:** identyfikator modelu wykonującego zadanie.
- **JSON:** format danych czytelny dla programów.
- **Retencja:** okres przechowywania danych.
- **Opt-out z treningu:** rezygnacja z wykorzystania danych do ulepszania modeli, zgodnie z warunkami dostawcy.

---

## 11. Przydatne źródła

- [ElevenLabs — strona i logowanie](https://elevenlabs.io).
- [Dokumentacja ElevenLabs](https://elevenlabs.io/docs).
- [Cennik i dostępność funkcji](https://elevenlabs.io/pricing).
- [Pierwsze kroki z API](https://elevenlabs.io/docs/eleven-api/quickstart).
- [Przykład STT przez API](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/speech-to-text).
- [Polityka prywatności](https://elevenlabs.io/privacy-policy).

---

## Dodatek A — pierwsze zapytania API (dla chętnych)

Ten dodatek możesz wykonać po wprowadzeniu do Colaba. **Nie trzeba przepisywać ani rozumieć każdej linijki podczas pokazu.**

W osobnej komórce Colaba zainstaluj bibliotekę: `%pip install requests`. Do STT wgraj do bieżącej sesji swój plik i dopasuj jego nazwę w kodzie. Przykład zakłada plik `moj_glos.wav`; dla MP3 zmień tę nazwę.

### A1. STT z diarizacją — plik → tekst i JSON

```python
import json
from getpass import getpass
from pathlib import Path

import requests

api_key = getpass("Wklej swój klucz ElevenLabs API (ukryty): ").strip()
audio_path = Path("moj_glos.wav")

with audio_path.open("rb") as audio_file:
    response = requests.post(
        "https://api.elevenlabs.io/v1/speech-to-text",
        headers={"xi-api-key": api_key},
        files={"file": (audio_path.name, audio_file)},
        data={
            "model_id": "scribe_v2",
            "language_code": "pol",
            "diarize": "true",
            "tag_audio_events": "false",
        },
        timeout=120,
    )

response.raise_for_status()
transcript = response.json()
print(transcript["text"])

Path("transkrypcja.txt").write_text(transcript["text"], encoding="utf-8")
Path("transkrypcja.json").write_text(
    json.dumps(transcript, ensure_ascii=False, indent=2), encoding="utf-8"
)

for word in transcript.get("words", []):
    if word.get("type") == "word":
        print(word.get("speaker_id"), word["start"], word["end"], word["text"])
```

Do sprawdzenia dwóch mówców podmień nazwę pliku na nagranie rozmowy. `diarize="true"` włącza oznaczenia mówców, a `speaker_id` pozwala odczytać je w wyniku. Plik TXT zapisuje tutaj sam tekst; pełna odpowiedź z czasami i mówcami pozostaje w JSON. Specyfikacja i przykład producenta: [STT API](https://elevenlabs.io/docs/api-reference/speech-to-text/convert), [STT quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/speech-to-text).

### A2. TTS — tekst → MP3

Uruchom jako osobny przykład. W polu `voice_id` wpisz identyfikator głosu dostępnego przez API na Twoim koncie. Aby użyć klonu, podaj jego identyfikator.

```python
from getpass import getpass
from pathlib import Path

import requests

api_key = getpass("Wklej swój klucz ElevenLabs API (ukryty): ").strip()
voice_id = input("Wklej voice_id wybranego głosu: ").strip()

response = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    headers={"xi-api-key": api_key},
    params={"output_format": "mp3_44100_128"},
    json={
        "text": "Cześć! Ten głos został wygenerowany z tekstu.",
        "model_id": "eleven_multilingual_v2",
    },
    timeout=120,
)

response.raise_for_status()
Path("wynik.mp3").write_bytes(response.content)
print("Zapisano wynik.mp3 — pobierz plik z panelu plików Colaba.")
```

`raise_for_status()` zatrzymuje przykład przy błędzie HTTP, zanim zapisze odpowiedź jako wynik. Parametry TTS: [Create speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert).

---

*Materiały: repo BrainHack2026_ASR_Workshop · AIMed AGH*

