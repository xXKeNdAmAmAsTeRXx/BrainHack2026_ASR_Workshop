# BrainHack 2026 — Warsztaty ASR 🎙️

Warsztaty z **rozpoznawania mowy (ASR — Automatic Speech Recognition)** uruchamianego **lokalnie** (bez chmury): od gotowych modeli po streaming w czasie rzeczywistym.

## Plan warsztatów

| # | Element | Opis | Dokument |
|---|---|---|---|
| 1 | **Wprowadzenie do ASR** | Czym jest ASR, architektury (CTC, seq2seq, transducer), historia: Kaldi → wav2vec 2.0 → Whisper | [docs/01_intro_asr.md](docs/01_intro_asr.md) |
| 2 | **Lokalne modele ASR** | Whisper (openai-whisper / faster-whisper), Vosk, wav2vec2 — instalacja, pierwsze transkrypcje, wybór modelu pod sprzęt | [docs/02_local_models.md](docs/02_local_models.md) |
| 3 | **Nagrywanie i streaming audio** | Wejście z mikrofonu (sounddevice), VAD, transkrypcja w czasie rzeczywistym | [docs/03_streaming.md](docs/03_streaming.md) |
| 4 | **Diaryzacja i przetwarzanie nagrań** | Kto mówi kiedy (pyannote), streszczanie długich nagrań, transkrypcja plików | [docs/04_diarization.md](docs/04_diarization.md) |
| 5 | **Ewaluacja i fine-tuning** | WER/CER, benchmark lokalnych modeli na polskim, fine-tuning wav2vec2 (wykład rozszerzony) | [docs/05_evaluation.md](docs/05_evaluation.md) |

## Struktura repo

```
├── README.md                  # ten plik — plan i zakładka repo
├── nbutil/                    # narzędzia pomocnicze do notebooków
├── Local_ASR_models.ipynb     # notatnik: lokalne modele ASR (Whisper, Vosk, wav2vec2)
└── docs/                      # dokumenty per element warsztatu (opis, wymagania, linki)
```

## Wymagania ogólne

- Python 3.10+ (polecamy środowisko przez `uv` lub `venv`)
- FFmpeg w PATH (dla whisper/audio)
- GPU przyspiesza mocno, ale wszystko działa też na CPU (mniejsze modele)
- Szczegółowe zależności: patrz `docs/02_local_models.md`

## Materiały w trakcie przygotowania 🚧
- [ ] notebook `Local_ASR_models.ipynb` — uzupełnić sekcje
- [ ] nagrania przykładowe (PL)
- [ ] quiz / zadania na koniec

---
*Projekt na BrainHack 2026 — AIMed AGH.*
