# 2. Lokalne modele ASR

**Cel:** uruchomić 3 rodziny modeli lokalnie i zrozumieć trade-offy.

## Modele
| Model | Zalety | Wady | Rozmiar |
|---|---|---|---|
| **Whisper / faster-whisper** (openai-whisper, SYSTRAN) | bardzo dobra jakość PL, multi-task, timestamps | wolniejszy na CPU (oryginał) | tiny–large: 39 MB – 3 GB |
| **Vosk** (alphacep) | lekki, szybki, streaming-ready, 20 jęz. | starsza jakość | 50 MB – 1.8 GB |
| **wav2vec2** (HuggingFace) | fine-tuning prosty, CTC | wymaga WER-owych poprawek, brak timestamps | ~1 GB |

## Wymagania
```bash
pip install faster-whisper vosk torch transformers soundfile
# + FFmpeg w PATH (apt install ffmpeg / brew install ffmpeg)
```
- GPU (CUDA) opcjonalne; na CPU: faster-whisper `compute_type='int8'`
- Modele pobierają się przy pierwszym uruchomieniu (HuggingFace cache: `~/.cache/huggingface`)

## Notebook
`Local_ASR_models.ipynb` w katalogu głównym repo.

## Linki
- faster-whisper: https://github.com/SYSTRAN/faster-whisper
- openai-whisper: https://github.com/openai/whisper
- Vosk models: https://alphacephei.com/vosk/models
- wav2vec2 PL: https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-polish
