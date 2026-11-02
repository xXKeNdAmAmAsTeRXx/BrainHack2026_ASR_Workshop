# 1. Wprowadzenie do ASR — plan prezentacji (15 min)

**Prowadzący:** Franek  
**Odbiorcy:** koło psychologów, brak wiedzy programistycznej i AI  
**Cel:** wspólne słownictwo i mapa trzech zagadnień warsztatu (speech-to-text, text-to-speech, diarizacja) + ich połączenie + zastosowania w psychologii

---

## Metadata

| Pole | Wartość |
|---|---|
| Czas | 15 min |
| Prowadzący | Franek |
| Odbiorcy | koło psychologów, brak AI/programowania |
| Materiał towarzyszący | `docs/01_intro/handout.md` (do wysłania uczestnikom) |

---

## Slajdy z timingiem

| # | Czas | Tytuł | Notatki (numery poniżej) | Wizual |
|---|---|---|---|---|
| 1 | 0:00–2:00 | Czym jest ASR (Automatic Speech Recognition) | 1–2 | — |
| 2 | 2:00–5:30 | Trzy filary: STT, TTS, diaryzacja | 3–5 | — |
| 3 | 5:30–7:30 | Pipeline spotkania | 6 | — |
| 4 | 7:30–10:30 | Ograniczenia i zastosowania w psychologii | 9–10 | — |
| 5 | 10:30–13:00 | Jak to działa i jakość (WER/CER) | 7–8 | — |
| 6 | 13:00–15:00 | Podsumowanie i plan warsztatu | 11 | — |

*Czasy sumują się do 15 min. Notatki 1–11 poniżej są przypisane do sześciu slajdów.*

---

## Notatki dla prowadzącego (skrypt mówiony)

### Slajd 1 — Wprowadzenie do ASR
> „Cześć! Przez najbliższe 15 minut oswoimy trzy pojęcia, które będą przewijać się przez cały warsztat: jak komputer zamienia mowę na tekst, jak zamienia tekst na mowę, i jak rozpoznaje, kto mówi. Potem pokażę, jak to się łączy w jedno narzędzie i gdzie to ma zastosowanie w psychologii.”

### Slajd 2 — Czym jest ASR?
> „ASR to Automatic Speech Recognition — automatyczne rozpoznawanie mowy. To dziedzina, w której komputer 'słucha' dźwięku i zamienia go na tekst. Można o tym myśleć jak o niewidzialnym stenotypiście, który nigdy się nie męczy. Ważne: ASR najpierw daje tekst — dopiero potem (opcjonalnie) ktoś lub coś ten tekst analizuje.”

### Slajd 3 — Speech-to-text
> „Speech-to-text, czyli transkrypcja: mowa → tekst. Spotkacie to pod wieloma nazwami: STT, transkrypcja, rozpoznawanie mowy. Przykłady: napisy do filmów, dyktowanie na telefonie, notatki ze spotkań, polecenia głosowe. W warsztacie transkrybować będziemy własne nagrania.”

### Slajd 4 — Text-to-speech
> „Text-to-speech: tekst → mowa, czyli syntetyczny głos. Zastosowania: czytniki ekranu dla osób z niepełnosprawnościami wzroku, audiobooki, asystenci głosowi, powiadomienia. Voice cloning: z około minuty nagrania można stworzyć głos przypominający konkretną osobę. To potężne narzędzie — i wymaga zgody.”

### Slajd 5 — Diarizacja
> „Diarizacja odpowiada na pytanie: kto mówi i kiedy. Dzieli nagranie na fragmenty przypisane mówcom — zwykle etykietami 'Mówca 1', 'Mówca 2', nie imionami. Przykład: transkrypcja spotkania, gdzie widać, kto co powiedział.”

### Slajd 6 — Pipeline spotkania
> „Połączenie: nagranie → speech-to-text (tekst) + diarizacja (kto) → jedna transkrypcja z oznaczeniem mówców → streszczenie. To właśnie robią automatycznie ElevenLabs czy Fireflies, o których będzie mowa w bloku API.”

### Slajd 7 — Pod maską
> „Wysoki poziom: dźwięk → cechy (spektrogram) → model (sieć neuronowa) → tekst. Model uczy się na milionach godzin nagrań. Nie programujemy reguł 'jeśli dźwięk X, to litera Y' — model sam znajduje wzorce.”

### Slajd 8 — WER i CER
> „Jak mierzymy jakość? WER = błędy słów / wszystkie słowa referencyjne. CER to samo na poziomie znaków. Mniej = lepiej, 0% = idealnie. Dobra transkrypcja czystej mowy to często 5–10% WER. Hałas i akcenty pogarszają wynik. W warsztacie policzymy to na własnych nagraniach (jiwer).”

### Slajd 9 — Zastosowania w psychologii
> „Gdzie to przydaje się w psychologii? Transkrypcja wywiadów badawczych i sesji — za zgodą; analiza jakościowa i kodowanie; dzienniki głosowe i EMA; text-to-speech dla psychoedukacji i dostępności; notatki ze spotkań i supervision. Zawsze z myślą o zgodzie i poufności.”

### Slajd 10 — Ograniczenia i prywatność
> „Pułapki: szum, nakładanie się mów, akcenty, żargon; utrata emocji i prozodii w tekście; halucynacje (model dopisuje); błędy zmieniające sens; bias w danych. I prywatność: gdzie idą dane — do chmury dostawcy czy zostają lokalnie? Zgoda pacjenta/klienta, tajemnica zawodowa. Szczegóły w bloku 4 — lokalny Whisper.”

### Slajd 11 — Podsumowanie
> „Trzy pojęcia w trzech słowach: mowa→tekst (STT), tekst→mowa (TTS), kto mówi kiedy (diarizacja). Dalej: rozwiązania chmurowe, Python/Colab, modele lokalne. Pytania zbierzemy w module 5.”

---

## Notatki dla prowadzącego

- Używaj analogii, unikaj żargonu; definiuj każdy termin przy pierwszym użyciu.
- Nie wchodź w szczegóły techniczne (architektury modeli) — to moduł 4.
- Jeśli czas się kończy: skróć „pod maską” (slajd 7) i WER/CER (slajd 8), zostaw definicje.
- Jeśli więcej czasu: pokaż krótki przykład transkrypcji (ale demo jest w module 4).
- Podkreśl zgodę i tajemnicę zawodową (psychologia) — to kluczowy punkt etyczny.
- Zakończ pytaniem retorycznym: „Kiedy wolno nagrać sesję?”

---

## Ryzyka

- Za dużo treści na 15 min → trzymać się tabeli timingowej.
- Odbiorcy bez AI → nie używać skrótów bez wyjaśnienia.
- Linki mogą się zmienić → sprawdzić przed warsztatem.

---

## Mapa do handoutu

| Notatka | Sekcja handoutu |
|---|---|
| 1 | 1. Czym jest ASR? |
| 2 | 1. Czym jest ASR? |
| 3 | 2. Trzy filary — STT |
| 4 | 2. Trzy filary — TTS |
| 5 | 2. Trzy filary — diarizacja |
| 6 | 3. Jak to się łączy |
| 7 | 4. Jak to działa |
| 8 | 5. Jakość: WER i CER |
| 9 | 6. Zastosowania w psychologii |
| 10 | 7–8. Ograniczenia i prywatność |
| 11 | 11. Co dalej w warsztacie |