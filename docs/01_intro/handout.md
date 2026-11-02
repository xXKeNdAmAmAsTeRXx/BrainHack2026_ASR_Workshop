# Wprowadzenie do ASR — materiał dla uczestników

**Warsztaty BrainHack 2026 — Rozpoznawanie i generowanie mowy**  
Moduł 1 (15 min) · Prowadzący: Franciszek Kubala, Mateusz Poszelężny - KN AIMed AGH

> Ten materiał towarzyszy wprowadzeniu. Znajdziesz tu definicje, przykłady, słownik pojęć i linki do źródeł. Nie wymaga wiedzy programistycznej.

---

## 1. Czym jest ASR?

**ASR** (Automatic Speech Recognition) = **automatyczne rozpoznawanie mowy**.  
To dziedzina, w której komputer „słucha” dźwięku i zamienia go na tekst.

**Analogia:** wyobraź sobie niewidzialnego stenotypistę, który nigdy się nie męczy i potrafi przepisać godzinę mowy w kilka sekund.

**Ważne rozróżnienie:** ASR daje **tekst**. To dopiero pierwszy krok — potem tekst można analizować, streszczać, przeszukiwać. Samo „rozumienie” mowy to osobne zagadnienie.

---

## 2. Trzy filary

### 2.1 Speech-to-text (transkrypcja) — mowa → tekst

- **Definicja:** zamiana nagrania mowy na tekst pisany.
- **Synonimy:** STT, transkrypcja, rozpoznawanie mowy.
- **Przykłady:** napisy do filmów i seriali, dyktowanie na telefonie, notatki ze spotkań, polecenia głosowe („zadzwoń do…”), wyszukiwanie głosowe.
- **Analogia:** jakby ktoś przepisał nagranie słowo po słowie.

### 2.2 Text-to-speech (TTS) — tekst → mowa

- **Definicja:** zamiana tekstu na mowę — syntetyczny głos.
- **Zastosowania:** czytniki ekranu (dostępność dla osób z niepełnosprawnościami wzroku), audiobooki, asystenci głosowi, powiadomienia, nawigacja.
- **Voice cloning (klonowanie głosu):** z około minuty nagrania można stworzyć głos przypominający konkretną osobę.
- **Etyka:** klonowanie głosu wymaga **zgody** osoby, której głos klonujemy. Bez zgody to nadużycie (deepfake audio, oszustwa).

### 2.3 Diarizacja — kto mówi i kiedy

- **Definicja:** podział nagrania na fragmenty przypisane poszczególnym mówcom.
- **Co robi:** odpowiada na pytanie „kto mówił i kiedy” — zwykle etykietami (Mówca 1, Mówca 2), nie imionami.
- **Przykład:** transkrypcja spotkania, w której widać, kto co powiedział.
- **Analogia:** jakby ktoś rozdzielił dialog na role w scenariuszu.

---

## 3. Jak to się łączy (pipeline spotkania)

1. **Nagranie** spotkania.
2. **Speech-to-text** → tekst.
3. **Diarizacja** → kto mówił w którym momencie.
4. **Połączenie** → jedna transkrypcja z oznaczeniem mówców.
5. **Streszczenie** (często przez model językowy) → krótkie podsumowanie.

To właśnie robią automatycznie narzędzia takie jak ElevenLabs czy Fireflies (moduł 2 warsztatu).

---

## 4. Jak to działa (wysoki poziom, bez matematyki)

1. **Dźwięk** → komputer zamienia go na cechy (tzw. spektrogram — „obraz” dźwięku).
2. **Model** (sieć neuronowa) patrzy na te cechy i przewiduje tekst.
3. Model **uczy się** na milionach godzin nagrań — nie programujemy reguł „jeśli dźwięk X, to litera Y”.

**Wniosek:** jakość zależy od danych, na których model się uczył, i od jakości nagrania.

---

## 5. Jakość: WER i CER

- **WER** (Word Error Rate) = błędy słów / wszystkie słowa referencyjne.
- **CER** (Character Error Rate) = to samo, ale na poziomie znaków.
- **Interpretacja:** mniej = lepiej; 0% = idealnie.
- **Typowo:** dobra transkrypcja czystej mowy to ~5–10% WER. Hałas, akcenty, żargon pogarszają wynik.
- W warsztacie (moduł 4) policzymy WER/CER na własnych nagraniach (biblioteka `jiwer`).

---

## 6. Zastosowania w psychologii

- Transkrypcja wywiadów badawczych i sesji (za zgodą).
- Analiza jakościowa: kodowanie, tematy, motywy.
- Dzienniki głosowe i EMA (ecological momentary assessment).
- Text-to-speech: materiały psychoedukacyjne, dostępność.
- Notatki ze spotkań i supervision.
- **Zawsze:** zgoda i poufność (patrz sekcja 8).

---

## 7. Ograniczenia i pułapki

- Szum tła, nakładanie się mów, akcenty, żargon.
- Utrata emocji i prozodii (tekst nie oddaje tonu głosu).
- **Halucynacje:** model może „dopisać” słowa, których nie było w nagraniu.
- Błędy mogą zmieniać sens — ważne w kontekście klinicznym i badawczym.
- Bias: modele mogą być mniej dokładne dla niektórych grup (akcenty, dialekty).

---

## 8. Prywatność — co warto wiedzieć (zapowiedź)

- **Chmura (API):** audio trafia na serwery dostawcy — pytaj: gdzie (UE/USA), retencja, czy używane do treningu, opt-out.
- **Lokalnie (Whisper):** dane nie opuszczają Twojej maszyny/sesji Colab.
- **Psychologia:** zgoda pacjenta/klienta, tajemnica zawodowa, minimalizacja danych.
- Szczegóły i ćwiczenie: moduł 2 (prywatność ElevenLabs) i moduł 4 (Whisper lokalnie).

---

## 9. Słownik pojęć

| Pojęcie | Definicja |
|---|---|
| ASR | Automatic Speech Recognition — automatyczne rozpoznawanie mowy (mowa → tekst) |
| STT | Speech-to-text — zamiana mowy na tekst |
| TTS | Text-to-speech — zamiana tekstu na mowę (syntetyczny głos) |
| Voice cloning | Klonowanie głosu z krótkiego nagrania |
| Diarizacja | Podział nagrania na segmenty przypisane mówcom (kto mówi i kiedy) |
| Transkrypcja | Tekstowa wersja nagrania mowy |
| WER | Word Error Rate — błędy na poziomie słów |
| CER | Character Error Rate — błędy na poziomie znaków |
| Halucynacja | Gdy model „dopisuje” tekst, którego nie było w nagraniu |
| Model | System (sieć neuronowa) uczący się wzorców z danych |
| Dane treningowe | Nagrania/teksty, na których model się uczył |
| Latencja | Opóźnienie między mową a wynikiem |
| Czas rzeczywisty (real-time) | Przetwarzanie na bieżąco, bez czekania na koniec nagrania |
| Spektrogram | „Obraz” dźwięku używany przez modele |
| LLM | Large Language Model — model językowy (np. do streszczania transkrypcji) |
| API | Sposób komunikacji programu z usługą w chmurze |
| Chmura vs lokalnie | Czy przetwarzanie (i dane) odbywa się u dostawcy, czy na Twojej maszynie |

---

## 10. Przydatne źródła

**Podstawy:**

- Wikipedia — Automatic speech recognition: https://en.wikipedia.org/wiki/Automatic_speech_recognition
- Wikipedia — Speech synthesis: https://en.wikipedia.org/wiki/Speech_synthesis
- Wikipedia — Word error rate: https://en.wikipedia.org/wiki/Word_error_rate

**Whisper:**

- OpenAI Whisper (opis): https://openai.com/research/whisper
- Artykuł (paper): https://arxiv.org/abs/2212.04356
- GitHub openai/whisper: https://github.com/openai/whisper
- faster-whisper: https://github.com/SYSTRAN/faster-whisper

**Diarizacja:**

- pyannote: https://github.com/pyannote/pyannote-audio
- WhisperX: https://github.com/m-bain/whisperX

**Chmura / TTS:**

- ElevenLabs docs: https://elevenlabs.io/docs
- ElevenLabs privacy: https://elevenlabs.io/privacy

**Notatki ze spotkań:**

- Fireflies: https://fireflies.ai

**Dema (online):**

- Hugging Face — Whisper: https://huggingface.co/spaces/openai/whisper

**Środowisko warsztatu:**

- Google Colab: https://colab.research.google.com

**Prywatność (PL):**

- UODO (ochrona danych): https://uodo.gov.pl

---

## 11. Co dalej w warsztacie

| Moduł | Temat |
|---|---|
| 2 | Rozwiązania chmurowe (ElevenLabs, Fireflies) + prywatność |
| 3 | Python i Google Colab (praktyka) |
| 4 | Modele lokalne: Whisper w Colab, WER/CER, diarizacja |
| 5 | Podsumowanie i pytania |

---

*Materiały: repo BrainHack2026_ASR_Workshop · AIMed AGH*