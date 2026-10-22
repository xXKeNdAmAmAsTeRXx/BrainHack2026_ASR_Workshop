# Modele lokalne (Whisper) — materiał dla uczestników

**Warsztaty BrainHack 2026 — Rozpoznawanie i generowanie mowy**  
Moduł 4 (20 min) · Prowadzący: Franek · AIMed AGH

> Ten materiał towarzyszy części warsztatowej. Znajdziesz tu pojęcia, porównania i linki. Kod jest w notebooku `Local_ASR_models.ipynb` — nie musisz go pisać samodzielnie.

---

## 1. Co to „model lokalny” (Whisper)?

**Whisper** to model rozpoznawania mowy, który można uruchomić **u siebie** — na własnym komputerze albo w sesji Google Colab.

**Analogia:** tłumacz siedzący w pokoju z Tobą, a nie przez telefon do biura tłumaczeń.

**Kluczowe:** audio **nie jest wysyłane** do żadnego API dostawcy. Przetwarzanie odbywa się na maszynie, na której uruchamiasz model.

---

## 2. Chmura vs lokalnie

| Kwestia | Chmura (API) | Lokalnie (Whisper) |
|---|---|---|
| Gdzie idzie audio | Na serwery dostawcy | Zostaje na Twojej maszynie/Colabie |
| Retencja | Zależy od dostawcy (sprawdź politykę) | Ty decydujesz, co zachować |
| Trening modeli na Twoich danych | Możliwe (opt-out) | Nie dotyczy |
| Jakość | Często bardzo dobra | Dobra, zależy od modelu/hałasu |
| Czas i wygoda | Szybko, bez instalacji | Wymaga uruchomienia (Colab) |
| Koszt | Limity/płatności | Darmowe (Colab CPU) |
| Kontrola nad danymi | Ograniczona | Pełna |

**Wniosek:** wybór zależy od tego, co ważniejsze — wygoda/jakość czy prywatność/kontrola.

---

## 3. Prywatność i zgoda (psychologia)

Checklist przed nagraniem sesji/wywiadu:

- [ ] **Zgoda** pacjenta/klienta (świadoma, dobrowolna, odwołalna).
- [ ] **Cel** nagrania jasno określony.
- [ ] **Gdzie** trafi nagranie i transkrypcja (chmura czy lokalnie).
- [ ] **Kto** ma dostęp i przez jak długo (retencja).
- [ ] **Anonimizacja** / pseudonimizacja w notatkach.
- [ ] **Tajemnica zawodowa** i minimalizacja danych.

**Zasada:** jeśli nagranie jest wrażliwe — preferuj model lokalny i nie wysyłaj audio do chmury bez podstawy prawnej.

---

## 4. Jak to wygląda w praktyce (Colab) — bez kodu

1. Otwórz notebook `Local_ASR_models.ipynb` w Google Colab.
2. Uruchom komórkę instalacyjną (jeden raz).
3. Wgraj własne nagranie (~1 min).
4. Uruchom transkrypcję (model działa w sesji Colab).
5. Zapisz wynik do pliku i pobierz na dysk.

**Gdzie kod:** w notebooku — wystarczy uruchamiać komórki (`Shift+Enter`). Nie musisz pisać kodu samodzielnie.

---

## 5. Zapis transkrypcji

- **txt** — zwykły tekst. Do archiwum, analizy jakościowej, cytatów.
- **SRT** — napisy z znacznikami czasu (format `HH:MM:SS,mmm`). Do wideo, do odsłuchiwania konkretnych fragmentów.

**Po co zapisywać:** archiwum, weryfikacja, cytowanie, analiza.

---

## 6. Jakość: WER i CER

- **WER** (Word Error Rate) = błędy słów / wszystkie słowa referencyjne.
- **CER** (Character Error Rate) = to samo na poziomie znaków.
- **Interpretacja:** mniej = lepiej; 0% = idealnie.
- **Typowo:** dobra transkrypcja czystej mowy to ~5–10% WER.
- **Co wpływa:** szum, akcenty, żargon, nakładanie się mów, jakość nagrania.

**Jak liczymy w warsztacie:** porównujemy ręczną transkrypcję (reference) z wynikiem modelu (hypothesis) — biblioteka `jiwer`.

---

## 7. Diaryzacja — skrót

- **Co to:** „kto mówi i kiedy” — podział nagrania na segmenty przypisane mówcom.
- **Lokalnie:** np. WhisperX lub pyannote (wymaga więcej zasobów i często tokena Hugging Face).
- **Dziś:** pokazujemy ideę; szczegóły i eksperymenty — samodzielnie (notebook, docs).

---

## 8. Kiedy chmura, kiedy lokalnie?

Wybierz **lokalnie**, gdy:
- nagranie jest wrażliwe (sesje, wywiady, dane pacjentów),
- potrzebujesz pełnej kontroli nad danymi,
- nie masz podstawy prawnej do wysyłania audio do chmury.

Wybierz **chmurę**, gdy:
- zależy Ci na wygodzie i szybkości,
- jakość musi być najwyższa (np. trudny akcent, żargon),
- masz zgodę i spełnione wymogi prawne.

---

## 9. Słownik pojęć

| Pojęcie | Definicja |
|---|---|
| Model lokalny | Model działający na Twojej maszynie/Colabie, bez wysyłania audio |
| Chmura (cloud) | Przetwarzanie na serwerach dostawcy |
| Retencja | Jak długo dane są przechowywane |
| Opt-out z treningu | Wyłączenie użycia danych do trenowania modeli |
| WER | Word Error Rate — błędy na poziomie słów |
| CER | Character Error Rate — błędy na poziomie znaków |
| SRT | Format napisów z znacznikami czasu |
| Colab | Google Colab — notebook w chmurze Google |
| HF token | Token Hugging Face (dostęp do modeli) |
| Diaryzacja | Podział nagrania na segmenty przypisane mówcom |

---

## 10. Przydatne źródła

- faster-whisper: https://github.com/SYSTRAN/faster-whisper
- openai-whisper: https://github.com/openai/whisper
- jiwer (WER/CER): https://github.com/jitsi/jiwer
- WhisperX: https://github.com/m-bain/whisperX
- pyannote: https://github.com/pyannote/pyannote-audio
- Google Colab: https://colab.research.google.com
- Whisper (paper): https://arxiv.org/abs/2212.04356

---

## 11. Co dalej

- Notebook `Local_ASR_models.ipynb` — uruchom w Colab na własnym nagraniu.
- Moduł 5 — podsumowanie i pytania.

---

*Materiały: repo BrainHack2026_ASR_Workshop · AIMed AGH*