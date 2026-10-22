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

| # | Czas | Tytuł | Kluczowe punkty (mówione) | Wizual |
|---|---|---|---|---|
| 1 | 0:00–0:30 | Wprowadzenie do ASR | Agenda: 3 pojęcia, jak działają razem, zastosowania w psychologii | tytuł + 3 ikony |
| 2 | 0:30–0:45 | Czym jest ASR? | Automatyczne rozpoznawanie mowy; komputer „słucha” i zapisuje tekst; analogia: niewidzialny stenotypista; najpierw tekst, potem analiza | fala dźwięku → tekst |
| 3 | 0:45–1:20 | Speech-to-text (transkrypcja) | Definicja mowa→tekst; synonimy STT/transkrypcja; przykłady: napisy, dyktowanie, notatki ze spotkań, polecenia głosowe | mikrofon → dokument |
| 4 | 1:20–2:20 | Text-to-speech (TTS) | tekst→mowa; zastosowania: czytniki ekranu, audiobooki, asystenci, powiadomienia; voice cloning z ~1 min nagrania + etyka/zgoda | tekst → fala dźwięku |
| 5 | 2:20–3:20 | Diarizacja (kto mówi i kiedy) | Podział nagrania na segmenty przypisane mówcom; etykiety (Mówca 1/2), nie imiona; przykład transkrypcji spotkania | timeline z kolorami mówców |
| 6 | 3:20–4:20 | Jak to się łączy: pipeline spotkania | Nagranie → STT (tekst) + diarizacja (kto) → połączona transkrypcja → streszczenie; podgląd bloku API (ElevenLabs) i Fireflies | flowchart |
| 7 | 4:20–4:55 | Jak to działa „pod maską” (wysoki poziom) | Dźwięk → cechy (spektrogram) → model (sieć neuronowa) → tekst; uczenie na milionach godzin; nie programujemy reguł | spektrogram → tekst |
| 8 | 4:55–5:30 | Jakość: WER i CER | WER = błędy słów / wszystkie słowa; CER = na znakach; mniej = lepiej; 0% = idealnie; typowo czysta mowa 5–10% WER; mierzymy (jiwer w warsztacie) | wzór + przykład |
| 9 | 5:30–6:30 | Zastosowania w psychologii | Transkrypcja wywiadów badawczych i sesji (za zgodą); analiza jakościowa/kodowanie; dzienniki głosowe/EMA; TTS: psychoedukacja, dostępność; notatki ze spotkań/supervision | lista |
| 10 | 6:30–7:55 | Ograniczenia i pułapki + prywatność (zapowiedź) | Szum, nakładanie się mów, akcenty, żargon; utrata emocji/prozodii; halucynacje; błędy zmieniają sens; bias; gdzie idą dane: chmura vs lokalnie; zgoda pacjenta/klienta, tajemnica zawodowa; zapowiedź bloku 4 (Whisper lokalnie) | „uwaga” + chmura vs laptop |
| 11 | 7:55–8:30 (bufor) | Podsumowanie i mapa warsztatu | 3 pojęcia w 3 słowach; co dalej (moduły 2–5); pytania na koniec modułu 5 | mapa |

*Czasy sumują się do ~8:30, zostaje ~6,5 min buforu na pytania/przejścia.*

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

| Slajd | Sekcja handoutu |
|---|---|
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