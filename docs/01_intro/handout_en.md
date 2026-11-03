# Introduction to ASR — participant handout

**BrainHack 2026 Workshop — Speech Recognition and Generation**  
Module 1 (15 min) · Instructors: Franciszek Kubala, Mateusz Poszelężny — KN AIMed AGH

> This material accompanies the introduction. You will find definitions, examples, a glossary and links to sources. No programming knowledge is required.

---

## 1. What is ASR?

**ASR** (Automatic Speech Recognition) is the field in which a computer "listens" to audio and turns it into text.

**Analogy:** imagine an invisible stenographer who never gets tired and can transcribe an hour of speech in seconds.

**Important distinction:** ASR produces **text**. That is only the first step — the text can then be analyzed, summarized, and searched. "Understanding" speech itself is a separate problem.

---

## 2. Three pillars

### 2.1 Speech-to-text (transcription) — speech → text

- **Definition:** converting a speech recording into written text.
- **Synonyms:** STT, transcription, speech recognition.
- **Examples:** subtitles for films and series, dictation on your phone, meeting notes, voice commands ("call…"), voice search.
- **Analogy:** as if someone transcribed the recording word for word.

### 2.2 Text-to-speech (TTS) — text → speech

- **Definition:** converting text into speech — a synthetic voice.
- **Applications:** screen readers (accessibility for people with visual impairments), audiobooks, voice assistants, notifications, navigation.
- **Voice cloning:** from about a minute of audio, you can create a voice resembling a specific person.
- **Ethics:** voice cloning requires the **consent** of the person whose voice is being cloned. Without consent it is abuse (audio deepfakes, fraud).

### 2.3 Diarization — who speaks and when

- **Definition:** splitting a recording into segments assigned to individual speakers.
- **What it does:** answers the question "who spoke and when" — usually with labels (Speaker 1, Speaker 2), not names.
- **Example:** a meeting transcript showing who said what.
- **Analogy:** as if someone split a dialogue into roles in a screenplay.

---

## 3. How it all fits together (meeting pipeline)

1. **Record** the meeting.
2. **Speech-to-text** → text.
3. **Diarization** → who spoke at which moment.
4. **Merge** → one transcript with speaker labels.
5. **Summarize** (often with a language model) → a short summary.

This is exactly what tools like ElevenLabs or Fireflies do automatically (workshop module 2).

---

## 4. How it works (high level, no math)

1. **Audio** → the computer converts it into features (a so-called spectrogram — an "image" of sound).
2. **A model** (a neural network) looks at these features and predicts the text.
3. The model **learns** from millions of hours of recordings — we do not program rules like "if sound X, then letter Y".

**Takeaway:** quality depends on the data the model was trained on and on the recording quality.

---

## 5. Quality: WER and CER

- **WER** (Word Error Rate) = word errors / all reference words.
- **CER** (Character Error Rate) = the same, but at the character level.
- **Interpretation:** lower is better; 0% = perfect.
- **Typically:** a good transcription of clean speech is ~5–10% WER. Noise, accents and jargon make results worse.
- In the workshop (module 4) we will compute WER/CER on our own recordings (the `jiwer` library).

---

## 6. Applications in psychology

- Transcribing research interviews and sessions (with consent).
- Qualitative analysis: coding, themes, motives.
- Voice diaries and EMA (ecological momentary assessment).
- Text-to-speech: psychoeducational materials, accessibility.
- Meeting and supervision notes.
- **Always:** consent and confidentiality (see section 8).

---

## 7. Limitations and pitfalls

- Background noise, overlapping speech, accents, jargon.
- Loss of emotion and prosody (text does not convey tone of voice).
- **Hallucinations:** the model may "add" words that were not in the recording.
- Errors can change meaning — important in clinical and research contexts.
- Bias: models may be less accurate for some groups (accents, dialects).

---

## 8. Privacy — what to know (a preview)

- **Cloud (API):** audio goes to the provider's servers — ask: where (EU/USA), retention, whether it is used for training, opt-out.
- **Locally (Whisper):** data never leaves your machine / Colab session.
- **Psychology:** patient/client consent, professional confidentiality, data minimization.
- Details and exercise: module 2 (ElevenLabs privacy) and module 4 (local Whisper).

---

## 9. Glossary

| Term | Definition |
|---|---|
| ASR | Automatic Speech Recognition — converting speech to text |
| STT | Speech-to-text — converting speech into text |
| TTS | Text-to-speech — converting text into speech (a synthetic voice) |
| Voice cloning | Cloning a voice from a short recording |
| Diarization | Splitting a recording into segments assigned to speakers (who speaks and when) |
| Transcription | The text version of a speech recording |
| WER | Word Error Rate — errors at the word level |
| CER | Character Error Rate — errors at the character level |
| Hallucination | When the model "adds" text that was not in the recording |
| Model | A system (neural network) that learns patterns from data |
| Training data | Recordings/texts the model was trained on |
| Latency | Delay between speech and the result |
| Real-time | Processing on the fly, without waiting for the recording to end |
| Spectrogram | An "image" of sound used by models |
| LLM | Large Language Model — a language model (e.g. for summarizing transcripts) |
| API | How a program communicates with a cloud service |
| Cloud vs local | Whether processing (and data) happens at the provider or on your machine |

---

## 10. Useful sources

**Basics:**

- Wikipedia — Automatic speech recognition: https://en.wikipedia.org/wiki/Automatic_speech_recognition
- Wikipedia — Speech synthesis: https://en.wikipedia.org/wiki/Speech_synthesis
- Wikipedia — Word error rate: https://en.wikipedia.org/wiki/Word_error_rate

**Whisper:**

- OpenAI Whisper (description): https://openai.com/research/whisper
- Paper: https://arxiv.org/abs/2212.04356
- GitHub openai/whisper: https://github.com/openai/whisper
- faster-whisper: https://github.com/SYSTRAN/faster-whisper

**Diarization:**

- pyannote: https://github.com/pyannote/pyannote-audio
- WhisperX: https://github.com/m-bain/whisperX

**Cloud / TTS:**

- ElevenLabs docs: https://elevenlabs.io/docs
- ElevenLabs privacy: https://elevenlabs.io/privacy

**Meeting notes:**

- Fireflies: https://fireflies.ai

**Demos (online):**

- Hugging Face — Whisper: https://huggingface.co/spaces/openai/whisper

**Workshop environment:**

- Google Colab: https://colab.research.google.com

**Privacy (Polish regulator):**

- UODO (data protection authority, Poland): https://uodo.gov.pl

---

## 11. What's next in the workshop

| Module | Topic |
|---|---|
| 2 | Cloud solutions (ElevenLabs, Fireflies) + privacy |
| 3 | Python and Google Colab (hands-on) |
| 4 | Local models: Whisper in Colab, WER/CER, diarization |
| 5 | Summary and questions |

---

*Materials: BrainHack2026_ASR_Workshop repo · AIMed AGH*
