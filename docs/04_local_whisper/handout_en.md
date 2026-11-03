# Local models (Whisper) — participant handout

**BrainHack 2026 Workshop — Speech Recognition and Generation**  
Module 4 (30 min) · Instructors: Franciszek Kubala, Mateusz Poszelężny — KN AIMed AGH

> This material accompanies the hands-on part. You will find concepts, comparisons and links here. The code is in the `Local_ASR_models.ipynb` notebook — you do not have to write it yourself.

---

## 1. What is a "local model" (Whisper)?

**Whisper** is a speech recognition model that you can run **on your own machine**, on your own computer. In a Google Colab session the same model runs, but on a Google machine — so that is already the cloud.

**Analogy:** an interpreter sitting in the room with you, rather than reached by phone at a translation agency.

**Key point:** Whisper does not send audio to an ASR provider's API. But **where the file lives depends on where you run it:**

- **Your own computer** — the audio stays with you.
- **Google Colab** — the model runs without an ASR API, but the file goes to a Google machine. Colab is the cloud, not "local".
- **API (ElevenLabs)** — the audio goes to the ASR provider's servers.

---

## 2. Cloud vs local

| Question | Cloud (API, e.g. ElevenLabs) | Colab (Whisper in the Google cloud) | Own computer (Whisper) |
|---|---|---|---|
| Where the audio goes | To the ASR provider's servers | To a Google machine, without an ASR API | Stays on your computer |
| Retention | Depends on the provider (check the policy) | Depends on Google and the session; files disappear from the session when it ends | You decide what to keep |
| Training models on your data | Possible (opt-out) | Check Google's terms | Not applicable |
| Quality | Often very good | Depends on the model and resources | Depends on the model and resources |
| Time and convenience | Fast, no installation | No installation, in the browser | Requires installation |
| Cost | Limits/payments | Free limits | Free (depends on hardware) |
| Control over data | Limited | Limited | Full |

**Takeaway:** the choice depends on what matters more — convenience/quality or privacy/control. If the recording is sensitive, only your own computer remains.

---

## 3. Privacy and consent (psychology)

Checklist before recording a session/interview:

- [ ] Patient/client **consent** (informed, voluntary, revocable).
- [ ] A clearly defined recording **purpose**.
- [ ] **Where** the recording and transcript will go (cloud or local).
- [ ] **Who** has access and for how long (retention).
- [ ] **Anonymization** / pseudonymization in notes.
- [ ] **Professional confidentiality** and data minimization.

**Rule:** if the recording is sensitive — prefer a local model and do not send audio to the cloud without a legal basis.

---

## 4. What it looks like in practice (Colab) — without code

1. Open the `Local_ASR_models.ipynb` notebook in Google Colab.
2. Run the installation cell (once).
3. Upload your own recording (~1 min).
4. Run the transcription (the model runs in the Colab session).
5. Save the result to a file and download it to your disk.

**Where the code is:** in the notebook — you just run the cells (`Shift+Enter`). You do not have to write code yourself.

---

## 5. Saving the transcript

- **txt** — plain text. For archives, qualitative analysis, quotations.
- **SRT** — subtitles with timestamps (format `HH:MM:SS,mmm`). For video, for listening back to specific fragments.

**Why save:** archiving, verification, quoting, analysis.

---

## 6. Quality: WER and CER

- **WER** (Word Error Rate) = word errors / all reference words.
- **CER** (Character Error Rate) = the same at the character level.
- **Interpretation:** lower is better; 0% = perfect.
- **Typically:** a good transcription of clean speech is ~5–10% WER.
- **What affects it:** noise, accents, jargon, overlapping speech, recording quality.

**How we compute it in the workshop:** we compare a manual transcript (reference) with the model's output (hypothesis) — the `jiwer` library.

---

## 7. Diarization — in brief

- **What it is:** "who speaks and when" — splitting a recording into segments assigned to speakers.
- **Locally:** e.g. WhisperX or pyannote (requires more resources and often a Hugging Face token).
- **Today:** we show the idea; details and experiments — on your own (notebook, docs).

---

## 8. When cloud, when local?

Choose **local** when:

- the recording is sensitive (sessions, interviews, patient data),
- you need full control over the data,
- you have no legal basis for sending audio to the cloud.

Choose **cloud** when:

- convenience and speed matter,
- quality must be top (e.g. a difficult accent, jargon),
- you have consent and the legal requirements are met.

---

## 9. Glossary

| Term | Definition |
|---|---|
| Local model | A model running on your own computer, without sending audio anywhere |
| Cloud | Processing on the provider's servers |
| Retention | How long data is stored |
| Training opt-out | Turning off the use of your data for training models |
| WER | Word Error Rate — errors at the word level |
| CER | Character Error Rate — errors at the character level |
| SRT | A subtitle format with timestamps |
| Colab | Google Colab — a notebook in the Google cloud |
| HF token | A Hugging Face token (access to models) |
| Diarization | Splitting a recording into segments assigned to speakers |

---

## 10. Useful sources

- faster-whisper: https://github.com/SYSTRAN/faster-whisper
- openai-whisper: https://github.com/openai/whisper
- jiwer (WER/CER): https://github.com/jitsi/jiwer
- WhisperX: https://github.com/m-bain/whisperX
- pyannote: https://github.com/pyannote/pyannote-audio
- Google Colab: https://colab.research.google.com
- Whisper (paper): https://arxiv.org/abs/2212.04356

---

## 11. What's next

- The `Local_ASR_models.ipynb` notebook — run it in Colab on your own recording.
- Module 5 — summary and questions.

---

*Materials: BrainHack2026_ASR_Workshop repo · AIMed AGH*
