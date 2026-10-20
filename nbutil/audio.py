"""Narzędzia audio: nagrywanie z mikrofonu, wczytywanie, normalizacja."""
"""(szkic — uzupełnimy na warsztacie)"""

def record(seconds=5, samplerate=16000):
    """Nagrywa `seconds` sekund z domyślnego mikrofonu (wymaga sounddevice)."""
    import sounddevice as sd
    import soundfile as sf
    audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write('recording.wav', audio, samplerate)
    return 'recording.wav'

def load(path):
    """Wczytuje plik audio jako (float32 array, samplerate)."""
    import soundfile as sf
    data, sr = sf.read(path, dtype='float32')
    return data, sr

def normalize(x):
    """Skaluje amplitudę do [-1, 1]."""
    m = abs(x).max()
    return x / m if m > 0 else x
