# 5. Ewaluacja i fine-tuning

**Cel:** zmierzyć jakość (WER) i pokazać ścieżkę fine-tuningu na polskich danych.

## Program
1. Metryki: **WER**, CER — wzory i pułapki (normalizacja, interpunkcja, liczby)
2. Benchmark lokalnych modeli na polskich nagraniach (zadanie warsztatowe)
3. Datasets: Common Voice PL, CLARIN-PL
4. Fine-tuning wav2vec2 na Common Voice (spacer po kodzie HF Trainer)

## Wymagania
```bash
pip install jiwer datasets transformers torch evaluate
```

## Linki
- jiwer (WER): https://github.com/jitsi/jiwer
- HF Audio course — fine-tuning: https://huggingface.co/learn/audio-course/chapter5/fine-tuning
- Common Voice PL dataset: https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0
- CLARIN-PL: https://clarin-pl.eu/

## Zadanie warsztatowe
Zmierz WER 3 modeli (whisper-small, vosk, wav2vec2-PL) na tym samym 1-minutowym nagraniu PL. Który wygrywa? Ile kosztuje czas transkrypcji vs jakość?
