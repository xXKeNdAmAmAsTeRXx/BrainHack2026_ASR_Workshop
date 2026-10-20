"""Narzędzia audio: wczytywanie, normalizacja, fragmentacja."""
"""(szkic — uzupełnimy na warsztacie)"""

def load(path):
    """Wczytuje plik audio jako (float32 array, samplerate)."""
    import soundfile as sf
    data, sr = sf.read(path, dtype='float32')
    return data, sr

def normalize(x):
    """Skaluje amplitudę do [-1, 1]."""
    m = abs(x).max()
    return x / m if m > 0 else x

def srt_time(t):
    """Sekundy -> 'HH:MM:SS,mmm' dla formatu SRT."""
    h, rem = divmod(t, 3600); m, s = divmod(rem, 60)
    return f'{int(h):02}:{int(m):02}:{int(s):02},{int((s%1)*1000):03}'
