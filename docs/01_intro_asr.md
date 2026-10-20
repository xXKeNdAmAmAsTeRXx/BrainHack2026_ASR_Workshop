# 1. Wprowadzenie do ASR

**Cel:** pokazać czym jest rozpoznawanie mowy, jak ewoluowały architektury i dlaczego dziś modele lokalne są realną alternatywą dla chmury.

## Program (30 min)
1. Pipeline ASR: audio → cechy (mel) → model → tekst
2. Architektury: **CTC** (wav2vec), **seq2seq/attention** (Whisper), **RNN-T** (streaming)
3. Historia: HMM/GMM → Kaldi → deep learning → Foundation models
4. Lokalnie vs chmura: prywatność (dane medyczne!), koszt, latencja
5. Polskie zasoby: Common Voice PL, CLARIN-PL, mowa PL

## Linki
- Omówienie ASR (HuggingFace course, PL tłumaczenie): https://huggingface.co/learn/audio-course/chapter5/introduction
- Whisper (paper): https://arxiv.org/abs/2212.04356
- wav2vec 2.0 (paper): https://arxiv.org/abs/2006.11477
- Kaldi: https://kaldi-asr.org/
- Common Voice PL: https://commonvoice.mozilla.org/pl/

## Wymagania
- brak — to sesja teoretyczna
