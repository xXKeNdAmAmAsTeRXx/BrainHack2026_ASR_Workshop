# 3. Nagrywanie i streaming audio

**Cel:** transkrypcja w czasie rzeczywistym z mikrofonu.

## Program
1. `sounddevice` — nagrywanie z mikrofonu (pomoce: `nbutil/audio.py`)
2. **VAD** (Voice Activity Detection): webrtcvad / silero-vad — wycinanie ciszy
3. Chunked inference: fragmenty 2–5 s → asystent pisze "na żywo"
4. Vosk streaming API (prawdziwy realtime, single chunk stream)

## Wymagania
```bash
pip install sounddevice soundfile webrtcvad
```
- mikrofon + uprawnienia systemowe
- test mikrofonu: `python -c "import sounddevice; print(sounddevice.query_devices())"`

## Linki
- sounddevice: https://python-sounddevice.readthedocs.io/
- silero-vad: https://github.com/snakers4/silero-vad
- Vosk streaming demo: https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py
