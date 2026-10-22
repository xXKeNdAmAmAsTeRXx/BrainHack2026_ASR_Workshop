# 2. ElevenLabs przez stronę i API — plan prezentacji (55 min)

**Prowadzący:** Mateusz  
**Odbiorcy:** koło psychologów, osoby początkujące, bez wiedzy programistycznej i AI  
**Cel:** uczestnicy wykonują STT na własnym nagraniu, sprawdzają diarizację rozmowy, generują mowę z tekstu oraz poznają klonowanie głosu i sposób uzyskania dostępu przez API.

> To scenariusz pokazu na żywo. Slajdy służą do wprowadzenia pojęć i poleceń; większość czasu pokazujesz stronę ElevenLabs.

**Stan instrukcji: 22 października 2026.** Przed warsztatem sprawdź interfejs na koncie, z którego będziesz prowadzić pokaz.

---

## Metadata

- **Czas:** 55 min, łącznie z ćwiczeniami i 2 min buforu.
- **Forma:** demonstracja w przeglądarce + krótkie zadania wykonywane równolegle przez uczestników.
- **Materiał towarzyszący:** [handout.md](handout.md) — instrukcje krok po kroku, słownik, źródła i opcjonalne przykłady API.
- **Wyniki:** transkrypcja własnego nagrania, sprawdzony podział rozmowy na mówców, plik TTS i znajomość miejsca tworzenia klucza API.
- **Klonowanie głosu:** pokaz na własnym głosie prowadzącego;

---

## Przygotowanie prowadzącego

- [ ] Zaloguj się wcześniej; zamknij prywatne projekty i powiadomienia. Powiększ interfejs, by tekst był czytelny z końca sali.
- [ ] Sprawdź dostęp do **Speech to Text**, **Text to Speech**, **Voices** oraz **Developers → API Keys**.
- [ ] Sprawdź limit konta. Do klonowania przygotuj konto z **Instant Voice Cloning**: według aktualnego cennika od Starter. Uczestnicy nie muszą kupować abonamentu. Źródło: [cennik](https://elevenlabs.io/pricing).
- [ ] Przygotuj czysty monolog własnego głosu lub innego nagrania, około 1–2 min
- [ ] Przećwicz odtwarzanie dźwięku z przeglądarki w sali.
- [ ] Otwórz wcześniej zakładki z narzędziami, cennikiem, dokumentacją API i ustawieniami wykorzystania danych.

**Ważne rozróżnienie materiałów:** monolog służy do STT i klonowania; dialog dwóch osób do diarizacji.

---

## Slajdy z timingiem

1. **0:00–2:00 — ElevenLabs: plan pokazu.** Krótka mapa zadań; co uczestnik zapisze na koniec.
2. **2:00–5:00 — Konto, limity.** Logowanie, omówienie limitów 
3. **5:00–9:00 — STT: wgranie własnego nagrania.** Demonstracja przesłania pliku i wyboru języka.
4. **9:00–16:00 — STT: sprawdzanie wyniku.** Odsłuch fragmentu, korekta i ćwiczenie uczestników.
5. **16:00–24:00 — Diarizacja: rozmowa dwóch osób.** Wgranie dialogu, etykiety i weryfikacja zmian mówcy.
6. **24:00–27:00 — Eksport transkrypcji.** Dobór formatu i sprawdzenie pobranego pliku.
7. **27:00–33:00 — TTS: generowanie mowy.** Tekst, głos, model; odsłuch i porównanie tempa.
8. **33:00–41:00 — Klonowanie własnego głosu.** Instant Voice Cloning i nowe zdanie wypowiedziane klonem.
9. **41:00–48:00 — Dostęp przez API.** Tworzenie klucza, uprawnienia 
10. **48:00–51:00 — Prywatność na koncie.** Kilka zdań na temat przechowywania danych i prywatności 
11. **51:00–53:00 — Podsumowanie i dalsza część warsztatu.** Sprawdzenie pojęć; przejście do Colaba i Whispera.
12. **53:00–55:00 — Pytania i bufor.** Dokończenie zapisu wyników lub ewentualnie pytania. 

**Łącznie: 55 min.**

---

## Notatki dla prowadzącego (skrypt mówiony i pokaz)

### Slajd 1 — ElevenLabs: plan pokazu

**Na slajdzie:** nagranie → tekst; rozmowa → mówcy; tekst → mowa; własny głos; API.

> „Teraz sprawdzimy te pojęcia na stronie ElevenLabs. Najpierw wgramy własne nagranie i przeczytamy wynik. Potem zobaczymy rozmowę podzieloną na mówców. W drugiej części wygenerujemy mowę z tekstu, pokażę klon swojego głosu i miejsce, w którym uzyskuje się dostęp dla programu. Do większości zadań wystarczy przeglądarka.”

**Działanie:** pokaż, gdzie uczestnicy znajdą handout. Zapowiedz, że polecenia będą pojawiały się pojedynczo, po krótkim pokazie.

### Slajd 2 — Konto, próbki i dane

**Na slajdzie:** konto + własny monolog + słuchawki; „Dane trafiają do chmury”.

> „Używamy neutralnych nagrań warsztatowych. Proszę nie wgrywać nagrań sesji ani historii zawierających poufne informacje. Mój plik służy do pokazu, a do klonowania użyję wyłącznie własnego głosu. Plan darmowy pozwala zacząć od STT i TTS w dostępnych limitach. Klonowanie pokażę na swoim koncie.”

**Pokaz:** sprawdź, czy grupa jest zalogowana i ma pliki. Krótko wskaż **Terms and privacy → Data use**. Wyjaśnij, że ustawienia wykorzystania danych warto sprawdzić przed pierwszą wysyłką; wrócicie do nich na końcu. Nie zmieniaj ustawień uczestników za nich.

**Czas dla grupy:** około 1 min na odnalezienie pliku i narzędzia. Osoba bez konta lub pliku może pracować w parze albo obserwować.

**Źródła:** [dostępność planów](https://elevenlabs.io/pricing), [ustawienia danych](https://elevenlabs.io/docs/help-center/legal/is-my-data-used-to-improve-eleven-labs-ai-models).

### Slajd 3 — STT: wgranie własnego nagrania

**Na slajdzie:** „Speech to Text → plik → język → transkrypcja”. Następnie przełącz na stronę.

> „Speech-to-text zamienia dźwięk w tekst. Na stronie wybieram plik i język; przetwarzanie wykona usługa. Nie musimy instalować modelu ani pisać programu.”

**Pokaz:** otwórz **Speech to Text → Transcribe files**, wybierz monolog, wskaż polski lub **Detect**, omów krótko **Tag audio events** i rozpocznij przez **Upload files**. Na stronie działa obecnie Scribe v2.

**Polecenie:** „Wgrajcie teraz swoje nagranie. Na razie zachowajcie domyślne opcje poza językiem”. Daj około 2 min na przesłanie pliku i uzyskanie wyniku.

**Źródło:** [instrukcja STT na stronie](https://elevenlabs.io/docs/eleven-creative/playground/speech-to-text).

### Slajd 4 — STT: sprawdzanie wyniku

**Na slajdzie:** „Odsłuchaj 15–20 sekund. Sprawdź liczby, nazwy i przeczenia”.

> „Czytelny tekst może zawierać błąd, który zmienia znaczenie. Dlatego odsłucham kawałek nagrania i porównam go z tekstem. Szczególnie interesują mnie liczby, nazwy i słowo «nie». Jeżeli wynik jest poprawny, też to odnotuję — nie będę szukać błędu na siłę.”

**Pokaz:** wybierz słowo w transkrypcji, odsłuchaj fragment i pokaż poprawkę w edytorze. Oddziel treść nagrania od ewentualnego streszczenia: tutaj sprawdzacie zapis tego, co padło.

**Ćwiczenie, około 4 min:** uczestnicy porównują krótki fragment, poprawiają błąd lub zaznaczają fragment sprawdzony. Zapytaj dwie osoby o obserwacje; nie wymagaj publicznego odtwarzania ich głosu.

**Efekt:** każdy potrafi wskazać fragment porównany z dźwiękiem.

**Źródło funkcji edytora:** [Speech to Text](https://elevenlabs.io/docs/eleven-creative/playground/speech-to-text).

### Slajd 5 — Diarizacja: rozmowa dwóch osób

**Na slajdzie:** krótki dialog z podpisami „Osoba A” i „Osoba B”. Wyjaśnij pojęcie, potem pokaż stronę.

> „Teraz poza tekstem interesuje nas, który mówca wypowiada dane zdanie. Użyję innego pliku, z dwiema osobami. Narzędzie nada im etykiety. Imiona możemy dopisać sami po odsłuchaniu, ale same etykiety nie potwierdzają tożsamości.”

**Pokaz:** wgraj przygotowany dialog. Otwórz wynik i wskaż mówców. W interfejsie podział jest częścią wyniku; nie obiecuj osobnego przełącznika. Pokaż edycję nazw w **Speakers**. W API odpowiednikiem włączenia diarizacji będzie `diarize=true`.

**Ćwiczenie, około 4 min:** grupa odsłuchuje co najmniej dwie zmiany osoby i sprawdza przypisania. Jeśli nie wszyscy mają dialog, pracujcie wspólnie na Twoim przykładzie. Zapytaj: „Czy tekst może być poprawny, a mówca przypisany błędnie?”.

**Efekt:** uczestnicy rozdzielają błąd transkrypcji od błędu diarizacji. Jeśli model połączy dwie osoby albo rozdzieli jedną na dwie etykiety, wykorzystaj to jako przykład ograniczenia.

**Źródła:** [mówcy w interfejsie](https://elevenlabs.io/docs/eleven-creative/playground/speech-to-text), [diarizacja w API](https://elevenlabs.io/docs/api-reference/speech-to-text/convert).

### Slajd 6 — Eksport transkrypcji

**Na slajdzie:** TXT — czytanie; SRT/VTT — napisy; JSON — dane dla programu.

> „Wybieramy format pod dalsze zadanie. Do czytania wystarczy tekst. Do napisów potrzebujemy czasu. Jeśli chcemy obrabiać wynik programem, przyda się struktura danych. Po pobraniu otwieramy plik i sprawdzamy, co rzeczywiście się zachowało.”

**Pokaz i zadanie:** otwórz **Export**, wybierz dostępny format i zapisz wynik. W pliku z rozmową sprawdź etykiety mówców; przy napisach pokaż czas. Jeśli wybrany eksport nie zawiera oznaczeń, wskaż inny wariant lub przygotowany JSON z API. Daj grupie około 1 min na zapis własnego wyniku.

**Źródła:** [formaty eksportu](https://elevenlabs.io/blog/how-to-transcribe-a-podcast), [odpowiedź JSON z API](https://elevenlabs.io/docs/api-reference/speech-to-text/convert).

### Slajd 7 — TTS: generowanie mowy

**Na slajdzie:** tekst z ćwiczenia C; głos + model; „Zmieniamy jeden parametr”.

> „Odwracamy kierunek: wpiszę tekst, a usługa wygeneruje nagranie. Wybieram głos i model obsługujący język polski. Głos określa brzmienie, a model wykonuje syntezę. Na początek nie musimy regulować wszystkich ustawień.”

**Pokaz:** otwórz **Text to Speech**, wklej przykład z handoutu, wybierz dostępny głos i model wielojęzyczny. Wygeneruj i odtwórz kilka sekund. Jeśli wybrany model ma **Speed**, zmień tempo, pozostawiając tekst, głos i model bez zmian. Pobierz audio.

**Ćwiczenie, około 3 min:** uczestnicy generują jedno krótkie nagranie; drugie tylko jeśli pozwala limit. Zapytaj: „Która wersja byłaby wygodniejsza jako instrukcja do ćwiczenia i dlaczego?”.

**Efekt:** uczestnicy zapisują plik audio i potrafią odróżnić wybór głosu od wyboru modelu.

**Źródło:** [Text to Speech — obsługa i ustawienia](https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech).

### Slajd 8 — Klonowanie własnego głosu

**Na slajdzie:** próbka własnego głosu → klon → nowy tekst; „Pokaz prowadzącego”.

> „Najpierw posłuchajcie kilku sekund mojego oryginalnego nagrania. Na jego podstawie utworzę głos do syntezy. Sprawdzimy go na zdaniu, którego nie przeczytałem w próbce. Dzięki temu usłyszymy nową wypowiedź wygenerowaną z tekstu. To przykład, dlaczego samo brzmienie głosu nie potwierdza, kto wypowiedział dane słowa.”

**Pokaz, około 5 min:** odtwórz oryginał. Przejdź do **Voices → + → Instant Voice Clone**, wgraj swój monolog, nazwij głos i potwierdź prawa oraz zgodę. Zapisz, wybierz **Use voice** i wygeneruj nowe zdanie z sekcji 7 handoutu. Porównaj oryginał z wynikiem.

**Rozmowa z grupą, około 3 min:** co jest podobne, a co brzmi inaczej? Podkreśl zgodę i oznaczanie syntetycznych nagrań. Professional Voice Cloning przedstaw tylko jako osobny, dłuższy proces.

**Źródła:** [Instant Voice Cloning](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning), [dostępność funkcji w planach](https://elevenlabs.io/pricing).

### Slajd 9 — Dostęp przez API

**Na slajdzie:** program → plik lub tekst + klucz → ElevenLabs → tekst lub audio. Obok trzy pojęcia: klucz API, `voice_id`, `model_id`.

> „Na stronie robiliśmy wszystko ręcznie. API pozwala zlecić te same typy zadań programowi. Klucz API daje dostęp do konta i jego limitów. Identyfikator głosu wybiera brzmienie, a identyfikator modelu — narzędzie do wykonania zadania.”

**Pokaz, około 4 min:**

1. Otwórz **Developers → API Keys** i formularz tworzenia klucza.
2. Wpisz nazwę warsztatową. Pokaż ograniczenia uprawnień i limit zużycia. Do tego przykładu wystarczą uprawnienia STT i TTS.
3. Przed utworzeniem i kopiowaniem klucza wstrzymaj udostępnianie ekranu albo pokaż przygotowany zrzut z ukrytą wartością. Uczestnicy mogą poprzestać na odnalezieniu formularza.
4. W **My Voices** wskaż menu **Copy voice ID**. Zaznacz, że dostęp do głosu przez API zależy od planu i rodzaju głosu.
5. Otwórz dokumentację STT i TTS. Wskaż, gdzie są dane wejściowe i przykład wyniku; nie omawiaj całej specyfikacji.

**Wyjaśnienie, około 3 min:** STT przyjmuje plik i zwraca tekst oraz dane w JSON; TTS przyjmuje tekst i zwraca audio. W dodatku A handoutu pokaż tylko miejsce na klucz, plik oraz wynik. Nie wymagaj teraz uruchamiania kodu; wprowadzenie do Colaba jest w kolejnym module. Poinformuj, że wysłanie zapytania korzysta z limitów konta, a utworzenie klucza samo nie uruchamia zadania.

**Efekt:** uczestnicy potrafią odnaleźć klucze API i rozróżnić trzy identyfikatory. Zainteresowani mają kompletny przykład do późniejszego wykonania.

**Źródła:** [klucze i uprawnienia](https://elevenlabs.io/docs/help-center/technical/how-do-i-authorize-myself-using-an-api-key), [voice ID](https://elevenlabs.io/docs/help-center/technical/how-do-i-find-the-voice-id-of-my-voices-via-the-website-and-api), [ograniczenia Voice Library](https://elevenlabs.io/docs/eleven-creative/voices/voice-library), [STT API](https://elevenlabs.io/docs/api-reference/speech-to-text/convert), [TTS API](https://elevenlabs.io/docs/api-reference/text-to-speech/convert).

### Slajd 10 — Prywatność na koncie

**Na slajdzie:** wykorzystanie do treningu; przechowywanie; usuwanie; miejsce przetwarzania.

> „Wróćmy do ustawień danych. Rezygnacja z wykorzystywania nowych danych do treningu to jedna sprawa, a przechowywanie i usunięcie plików to kolejne. Sprawdzajmy je osobno. Na dzisiejszy pokaz wybraliśmy neutralne materiały, ale przed użyciem zawodowym trzeba ustalić warunki dla konkretnego zastosowania.”

**Zadanie, około 2 min:** uczestnicy odszukują **Terms and privacy → Data use → Improve the models for everyone**. Wyjaśnij, jak zapisać wybór i że zgodnie z instrukcją dotyczy on nowych danych. Każdy sam decyduje o swoim ustawieniu. Następnie poproś grupę o wskazanie jednej informacji, którą trzeba jeszcze sprawdzić w polityce lub umowie: okres przechowywania, usuwanie albo region.

**Przejście:** zapowiedz Whispera. Dopowiedz: „Własny komputer i Colab to różne miejsca przetwarzania; Colab działa w chmurze Google”.

**Źródła:** [opt-out z treningu](https://elevenlabs.io/docs/help-center/legal/is-my-data-used-to-improve-eleven-labs-ai-models), [polityka prywatności](https://elevenlabs.io/privacy-policy).

### Slajd 11 — Podsumowanie i dalsza część warsztatu

**Na slajdzie:** zapisane wyniki + przejście do Colaba.

> „Mamy zapis mowy, wiemy, jak sprawdzić przypisanie mówców, i potrafimy wygenerować nagranie z tekstu. Pokaz klonowania pozwolił usłyszeć nową wypowiedź podobną do głosu z próbki. API daje programowi dostęp do tych zadań. Zachowajcie własne nagranie i sprawdzony tekst — porównamy je z wynikiem Whispera.”

**Szybkie sprawdzenie z grupą:**

- „Które narzędzie wybierzesz, żeby zamienić wywiad na tekst?” — STT.
- „Co sprawdzisz, gdy zdanie zapisano poprawnie, ale przypisano złej osobie?” — diarizację.
- „Co potrzebuje tekstu jako wejścia?” — TTS.
- „Czym różni się klucz API od identyfikatora głosu?” — dostęp do konta a wybór głosu.

**Przejście:** wskaż handout i jego dodatek API, potem oddaj głos osobie prowadzącej wprowadzenie do Pythona i Colaba.

### Slajd 12 — Pytania i bufor

Pozostaw 2 min na zapis plików, krótkie pytanie albo opóźnienie wcześniejszego pokazu. Jeśli nikt nie potrzebuje pomocy, zapytaj: „Które z tych zadań przydałoby się w waszej pracy i jak sprawdzilibyście wynik?”.

---

## Wskazówki do prowadzenia

- Najpierw pokaż jeden krok, potem daj czas na jego wykonanie. Nie przełączaj narzędzia, gdy grupa nadal przesyła pliki.
- Wyjaśniaj skróty przy pierwszym użyciu. Na ekranie API skup się na wejściu, wyjściu i kluczu; kod pozostaw w handoucie.
- Odtwarzaj krótkie fragmenty; do porównania zwykle wystarczy kilka sekund. Nie zachęcaj całej sali do jednoczesnego odtwarzania przez głośniki laptopów.
- Kiedy model popełni błąd, pokaż sposób jego zauważenia. Nie obiecuj, że każde kolejne przetworzenie go naprawi.

## Ryzyka i plan awaryjny

- **Brak internetu lub długie oczekiwanie:** pokaż wcześniej przygotowaną transkrypcję i odtwórz pobrane audio. Przejdź z grupą przez sprawdzanie wyniku.
- **Wyczerpany limit albo brak funkcji:** przejdź do wyniku prowadzącego; klonowanie pozostaje demonstracją.
- **Diarizacja nie rozdziela rozmówców:** odsłuchaj moment zmiany osoby i omów błąd; pokaż też przygotowany przykład z czytelnym podziałem.
- **Inny interfejs:** szukaj nazw funkcji zamiast położenia przycisków. Stosuj zamiennie angielskie/polskie nazwy. 
- **Brak czasu:** zrezygnuj z drugiej generacji TTS i omawiania kodu. Zachowaj pokaz wszystkich czterech funkcji oraz miejsca tworzenia klucza.

---

## Mapa do handoutu

- **Slajdy 1–2:** sekcje 1–2 — pojęcia, przygotowanie i limity; sekcja 9 — ustawienia danych.
- **Slajdy 3–4:** sekcja 3 — transkrypcja własnego głosu.
- **Slajd 5:** sekcja 4 — diarizacja i dialog do nagrania.
- **Slajd 6:** sekcja 5 — eksport wyników.
- **Slajd 7:** sekcja 6 — TTS.
- **Slajd 8:** sekcja 7 — klonowanie własnego głosu.
- **Slajd 9:** sekcja 8 i dodatek A — dostęp przez API oraz przykłady kodu.
- **Slajd 10:** sekcja 9 — prywatność.
- **Slajdy 11–12:** sekcje 10–13 — pomoc, słownik, źródła i dalsze moduły.

---

*Materiały: repo BrainHack2026_ASR_Workshop · AIMed AGH*
