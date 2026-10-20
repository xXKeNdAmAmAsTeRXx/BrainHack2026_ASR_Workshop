# 4. Diaryzacja i przetwarzanie nagrań

**Cel:** "kto mówi, kiedy" + praca z długimi nagraniami (spotkania, wykłady).

## Program
1. **Diarization**: pyannote.audio (speaker-diarization-3.1) — wymaga HF token
2. Łączenie diaryzacji + ASR = transkrypcja z mówcami ("Meeting minutes")
3. Long-form: chunking długich nagrań, streszczanie z LLM
4. Formaty eksportu: SRT/VTT (napisy)

## Wymagania
```bash
pip install pyannote.audio
```
- **HF token** (darmowy) + zaakceptowanie licencji modeli pyannote na HF
- GPU mocno zalecane dla diaryzacji

## Linki
- pyannote.audio: https://github.com/pyannote/pyannote-audio
- speaker-diarization-3.1: https://huggingface.co/pyannote/speaker-diarization-3.1
- WhisperX (ASR + diaryzacja w jednym): https://github.com/m-bain/whisperX
