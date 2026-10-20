# 4. Ochrona danych i modele lokalne — 20 min (Franek)

**Cel:** pokazać alternatywę chmurową: model lokalny = dane nie opuszczają Twojej maszyny/Colaba.

## Program (część warsztatowa w Colab)
1. **Ochrona danych** — porównanie z blokiem API: co zostaje u dostawcy vs lokalnie
2. **Whisper lokalnie w Colab**:
   - `pip install faster-whisper` / `openai-whisper`
   - transkrypcja **własnego nagrania** (speech-to-text)
   - **zapisanie transkrypcji do pliku** (txt / SRT)
3. **Metryki jakości: CER / WER** — wzory, liczenie na przykładzie (jiwer)
4. **Diaryzacja** — pyannote/whisperX na Colab (skrót)

## Notebook
`Local_ASR_models.ipynb` w repo — otwórz w Colab: *File → Open notebook → GitHub* (wklej URL repo) lub prześlij plik.

## Wymagania
```python
!pip install faster-whisper jiwer
```
- konto Google (Colab), własne nagranie (~1 min)

## Linki
- faster-whisper: https://github.com/SYSTRAN/faster-whisper
- openai-whisper: https://github.com/openai/whisper
- jiwer (WER/CER): https://github.com/jitsi/jiwer
- WhisperX (ASR + diaryzacja): https://github.com/m-bain/whisperX
- pyannote: https://github.com/pyannote/pyannote-audio
