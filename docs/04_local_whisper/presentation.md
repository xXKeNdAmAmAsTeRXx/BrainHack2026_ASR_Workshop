# 4. Ochrona danych i modele lokalne — plan prezentacji (30 min)

**Prowadzący:** Franek  
**Odbiorcy:** koło psychologów, brak wiedzy programistycznej i AI  
**Cel:** pokazać alternatywę chmurową — model lokalny = dane nie opuszczają Twojego komputera. Colab to chmura Google, nie lokalne środowisko. Prywatność, jakość, diaryzacja (opcjonalnie)

---

## Metadata

| Pole | Wartość |
|---|---|
| Czas | 30 min |
| Prowadzący | Franek |
| Odbiorcy | koło psychologów, brak AI/programowania |
| Materiał towarzyszący | `docs/04_local_whisper/handout.md` (uczestnicy), `Local_ASR_models.ipynb` (kod) |

---

## Slajdy z timingiem

| # | Czas | Tytuł | Notatki (numery poniżej) | Wizual |
|---|------|-------|--------------------------|--------|
| 1 | 0:00–6:00 | API vs Colab vs własny komputer | 1–4 | — |
| 2 | 6:00–18:00 | Whisper w Colab: instalacja, wgranie, transkrypcja, plik | 5–7 | — |
| 3 | 18:00–26:00 | WER/CER na własnym nagraniu i własnym reference | 8–9 | — |
| 4 | 26:00–30:00 | Porównanie z API; diaryzacja tylko przy zapasie czasu | 10–12 | — |

*Czasy sumują się do 30 min. Notatki 1–12 poniżej są przypisane do czterech bloków; notatka 10 (diaryzacja) jest opcjonalna.*

---

## Notatki dla prowadzącego (skrypt mówiony)

### Slajd 1 — Po co modele lokalne?
> „Zacznijmy od pytania: gdzie trafiają nasze nagrania, gdy używamy narzędzi w chmurze? Dziś pokażę trzy miejsca: API dostawcy, Colab i własny komputer. Różnią się tym, czyj jest serwer.”

### Slajd 2 — Chmura vs lokalnie
> „W API: audio trafia na serwery dostawcy — zostaje tam przez jakiś czas, może być użyte do treningu modeli. W Colabie: model działa bez API, ale plik trafia na maszynę Google, więc to nadal chmura. Tylko własny komputer zostawia audio u nas — my decydujemy, co zostaje.”

### Slajd 3 — Co to „model lokalny”?
> „Whisper to model rozpoznawania mowy, który możemy uruchomić u siebie. Analogia: tłumacz siedzący w pokoju, a nie przez telefon. Audio nie jest wysyłane do żadnego API.”

### Slajd 4 — Ochrona danych w psychologii
> „W pracy psychologicznej: zgoda pacjenta/klienta, tajemnica zawodowa, minimalizacja danych. Pytanie kluczowe: kiedy wolno nagrać sesję lub wywiad — i gdzie trafi to nagranie?”

### Slajd 5 — Whisper w Colab
> „Pokazujemy notebook krok po kroku: instalacja, wgranie nagrania, transkrypcja, zapis, pobranie. Nie musicie pisać kodu — wystarczy uruchamiać komórki.”

### Slajd 6 — Transkrypcja
> „Dostajemy tekst z znacznikami czasu, po polsku. To nie jest idealne — akcenty, szum i żargon bywają problemem.”

### Slajd 7 — Zapis do pliku
> „txt — zwykły tekst do archiwum/analizy. SRT — napisy z czasem (do wideo, do cytowania fragmentów).”

### Slajd 8 — WER i CER
> „Jak mierzymy jakość? WER = błędy słów / wszystkie słowa. CER = to samo na znakach. Mniej = lepiej, 0% = idealnie.”

### Slajd 9 — WER/CER na własnym nagraniu
> „Porównujemy ręczną transkrypcję (reference) z wynikiem modelu (hypothesis). Widzimy, co model pomylił — i dlaczego.”

### Slajd 10 — Diaryzacja (skrót)
> „Kto mówi i kiedy — lokalnie, np. WhisperX lub pyannote. Wymaga więcej zasobów i konfiguracji. Dziś pokazujemy ideę i odsyłamy do samodzielnych eksperymentów.”

### Slajd 11 — Porównanie z API
> „Jakość, czas, gdzie poszły dane. Chmura: wygodniej i często szybciej; lokalnie: kontrola i prywatność. Wybór zależy od przypadku.”

### Slajd 12 — Podsumowanie
> „Trzy wnioski: prywatność ma znaczenie; lokalnie = kontrola nad danymi; jakość warto mierzyć. Co dalej — notebook i moduł 5.”

---

## Notatki dla prowadzącego

- Trzymać się prostego języka; nie wchodzić w szczegóły modeli/architektury.
- Nie wymagać od uczestników pisania kodu — pokazujemy notebook krok po kroku.
- Podkreślić zgodę i tajemnicę zawodową (psychologia).
- Jeśli czas się kończy: skrócić diaryzację (slajd 10) i porównanie (slajd 11).
- Zakończyć pytaniem: „Kiedy wolisz, żeby nagranie nie opuściło Twojego komputera?”

## Ryzyka

- Colab może być wolny (CPU) → przygotować zrzuty ekranu jako backup.
- Uczestnicy mogą pytać o kod → odesłać do notebooka i docs.

---

## Mapa do handoutu

| Slajd | Sekcja handoutu |
|---|---|
| 1–2 | 1–2. Model lokalny / chmura vs lokalnie |
| 3 | 1. Co to model lokalny |
| 4 | 3. Prywatność i zgoda |
| 5–7 | 4–5. Praktyka / zapis |
| 8–9 | 6. Jakość WER/CER |
| 10 | 7. Diaryzacja |
| 11 | 8. Kiedy chmura, kiedy lokalnie |
| 12 | 11. Co dalej |