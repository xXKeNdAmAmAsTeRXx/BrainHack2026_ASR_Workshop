# BrainHack 2026 — Warsztaty ASR 🎙️

Warsztaty z **rozpoznawania i generowania mowy**: speech-to-text, text-to-speech i diaryzacja — od rozwiązań chmurowych (API) po lokalne modele (prywatność danych).

## Plan warsztatów

Slot: 3,5 h + 0,5 h przerwy. Rdzeń programu to 2 h; pozostały czas to zapas na część praktyczną.

| Czas                  | Element | Prowadzący | Materiały |
|-----------------------|---|---|---|
| **Wymagania wstępne** | konto ElevenLabs + nagranie własnego głosu (~1 min) — przed warsztatem | — | [docs/00_prerequisites.md](docs/00_prerequisites.md) |
| **15 min**            | Wprowadzenie do ASR (speech-to-text, text-to-speech, diaryzacja) | Franek | [01_wprowadzenie.pdf](01_wprowadzenie.pdf) (uczestnicy) · [prezentacja](docs/01_intro/presentation.md) (prowadzący) |
| **55 min**            | Rozwiązania przez API i strony — ElevenLabs (transkrypcja, diaryzacja, TTS, API) + prywatność danych | Mateusz | [02_elevenlabs.pdf](02_elevenlabs.pdf) (uczestnicy) · [prezentacja](docs/02_api_elevenlabs/presentation.md) (prowadzący) |
| **10 min**            | Krótki wstęp do Python i Google Colab | — | [03_colab.pdf](03_colab.pdf) (uczestnicy) · [prezentacja](docs/03_colab_intro/presentation.md) (prowadzący) |
| **30 min**            | Ochrona danych i modele lokalne — Whisper w Colab: transkrypcja, zapis do pliku, WER/CER | Franek | [04_whisper.pdf](04_whisper.pdf) (uczestnicy) · [prezentacja](docs/04_local_whisper/presentation.md) (prowadzący) · [notebook](Local_ASR_models.ipynb) |
| **10 min**            | Podsumowanie i pytania + kontakt AIMed | Franek i Mateusz | [docs/05_summary.md](docs/05_summary.md) |

**Przerwa:** 30 min (np. po bloku API).

**Opcje, tylko gdy zostanie czas:** Fireflies (notatki ze spotkań, moduł 2) i diaryzacja lokalna (moduł 4).

## Notatnik

[`Local_ASR_models.ipynb`](Local_ASR_models.ipynb) — lokalny Whisper w Google Colab. Otwórz w Colab: *File → Open notebook → GitHub* albo prześlij plik. Wgraj własne nagranie (~1 min) i własną transkrypcję referencyjną, jeśli chcesz policzyć WER/CER. Wersja angielska: [`Local_ASR_models_en.ipynb`](Local_ASR_models_en.ipynb).

## Struktura repo

```
├── 01_wprowadzenie.pdf          # handout modułu 1 (dla uczestników)
├── 02_elevenlabs.pdf            # handout modułu 2
├── 03_colab.pdf                 # handout modułu 3
├── 04_whisper.pdf               # handout modułu 4
├── Local_ASR_models.ipynb       # notatnik: lokalny Whisper w Colab
├── README.md
├── assets/
│   ├── aimed-logo.png           # logo KN AIMed AGH (patrz Licencja)
│   └── fonts/                   # Fira Sans, Fira Mono, M PLUS 1 + licencje OFL
├── scripts/
│   └── build_pdf.py             # składa handouty z docs/ do PDF w katalogu głównym
├── sample_data/                 # przykładowe nagranie (patrz Licencja)
└── docs/
    ├── 00_prerequisites.md
    ├── 0N_*.md                  # indeks modułu (linki do PDF i prezentacji)
    ├── 0N_*/handout.md          # źródło PDF dla uczestników
    └── 0N_*/presentation.md     # plan slajdów, timing i skrypt dla prowadzącego
```

## Generowanie PDF-ów

PDF-y w katalogu głównym są zacommitowane. Po zmianie w `docs/*/handout.md` złóż je ponownie:

```bash
uv run scripts/build_pdf.py
```

Zależności (`markdown`, `weasyprint`) instaluje `uv` automatycznie.

WeasyPrint wymaga bibliotek Pango w systemie. Szablon używa czcionek z `assets/fonts/` (ten sam zestaw co strona [brainhackkrakow.org](https://brainhackkrakow.org/)), więc PDF wygląda tak samo na każdej maszynie. DejaVu Sans jest tylko zapasowym krojem dla znaków, których brak w tych czcionkach (np. strzałka →).

Nagłówek każdej strony to pasek w kolorach Brainhack z logo AIMed i nazwą modułu. Nazwy modułów są w `scripts/build_pdf.py` (lista `HANDOUTS`).

## Przygotowanie (przed warsztatem)
1. **Załóż konto** na [elevenlabs.io](https://elevenlabs.io) (free tier wystarczy)
2. **Nagraj ~1 minutę własnego głosu** (przyda się do części TTS/voice cloning)
3. Konto Google (do Colab) — opcjonalnie, ale przydatne

## Licencja

Materiały warsztatu (dokumentacja w `docs/`, handouty PDF, skrypt `scripts/build_pdf.py`, notatnik `Local_ASR_models.ipynb`) są udostępnione na licencji [Creative Commons Uznanie autorstwa 4.0 Międzynarodowe (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pl). Możesz je kopiować, zmieniać i wykorzystywać, także komercyjnie, pod warunkiem podania autorstwa (KN AIMed AGH, BrainHack 2026) i informacji o zmianach.

**Wyjątki:**

- `sample_data/OCZYBOLA.WAV` to fragment filmu z darmowej biblioteki nagrań, bez licencji. Nie jest objęty CC BY 4.0 i nie jest referencją ćwiczeń warsztatu. Przed dalszym wykorzystaniem trzeba ustalić prawa do tego nagrania samodzielnie.
- `assets/aimed-logo.png` to znak KN AIMed AGH. Nie jest objęty CC BY 4.0. Przed użyciem poza tym repozytorium ustal zasady z KN AIMed AGH.
- `assets/fonts/` to Fira Sans, Fira Mono i M PLUS 1 na licencji SIL Open Font License 1.1 (teksty licencji w `assets/fonts/OFL-*.txt`). Pliki M PLUS 1 są przycięte do alfabetu łacińskiego i zapisane jako statyczne instancje wagi 400 i 700.

---
*Warsztaty BrainHack 2026 — AIMed AGH.*
