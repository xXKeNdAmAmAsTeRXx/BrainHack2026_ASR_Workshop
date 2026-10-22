# BrainHack 2026 — Warsztaty ASR 🎙️

Warsztaty z **rozpoznawania i generowania mowy**: speech-to-text, text-to-speech i diaryzacja — od rozwiązań chmurowych (API) po lokalne modele (prywatność danych).

## Plan warsztatów (3,5 h + 0,5 h przerwa)

| Czas                  | Element | Prowadzący | Dokument |
|-----------------------|---|---|---|
| **Wymagania wstępne** | konto ElevenLabs + nagranie własnego głosu (~1 min) — przed warsztatem | — | [docs/00_prerequisites.md](docs/00_prerequisites.md) |
| **15 min**            | Wprowadzenie do ASR (speech-to-text, text-to-speech, diaryzacja) | Franek | [docs/01_intro/handout.md](docs/01_intro/handout.md) (uczestnicy) · [docs/01_intro/presentation.md](docs/01_intro/presentation.md) (prowadzący) |
| **55 min**            | Rozwiązania dostępne przez API i strony — przykład: **ElevenLabs** (transkrypcja, transkrypcja+diaryzacja, TTS, kod przez API) + jak przechowywane/chronione są dane + Fireflies (notatki ze spotkań) | Mateusz | [docs/02_api_elevenlabs.md](docs/02_api_elevenlabs.md) |
| **10 min**            | Krótki wstęp do Python i Google Colab | — | [docs/03_colab_intro.md](docs/03_colab_intro.md) |
| **30 min**            | Ochrona danych i modele lokalne — część warsztatowa: lokalny **Whisper** w Colab (STT, zapis do pliku, CER/WER, diaryzacja) | Franek | [docs/04_local_whisper/handout.md](docs/04_local_whisper/handout.md) (uczestnicy) · [docs/04_local_whisper/presentation.md](docs/04_local_whisper/presentation.md) (prowadzący) |
| **10 min**            | Podsumowanie i pytania ("co wiem po warsztatach i co dalej?") + kontakt AIMed | Franek i Mateusz | [docs/05_summary.md](docs/05_summary.md) |

**Przerwa:** 30 min (np. po bloku API).

## Struktura repo

```
├── README.md                     # plan warsztatów i zakładka repo
├── Local_ASR_models.ipynb        # notatnik: lokalny Whisper w Colab (STT, WER/CER, diaryzacja)
├── sample_data/                  # przykładowe nagrania
└── docs/                         # materiały per element warsztatu (opis, wymagania, linki)
    ├── 00_prerequisites.md
    │   
    ├── 01_intro.md
    ├── 01_intro/
    │   ├── handout.md
    │   └── presentation.md
    │   
    ├── 02_api_elevenlabs.md
    ├── 02_api_elevenlabs/
    │   ├── handout.md
    │   └── presentation.md
    │   
    ├── 03_colab_intro.md
    ├── 03_colab_intro/ 
    │   ├── handout.md
    │   └── presentation.md
    │   
    ├── 04_local_whisper.md   
    ├── 04_local_whisper/
    │   ├── handout.md
    │   └── presentation.md
    │   
    └── 05_summary.md
```

## Przygotowanie (przed warsztatem)
1. **Załóż konto** na [elevenlabs.io](https://elevenlabs.io) (free tier wystarczy)
2. **Nagraj ~1 minutę własnego głosu** (przyda się do części TTS/voice cloning)
3. Konto Google (do Colab) — opcjonalnie, ale przydatne

## Materiały w trakcie przygotowania 🚧
- [ ] notebook `Local_ASR_models.ipynb` — uzupełnić sekcje
- [ ] przykładowe nagrania PL
- [ ] gotowe komórki API ElevenLabs

---
*Projekt na BrainHack 2026 — AIMed AGH.*
