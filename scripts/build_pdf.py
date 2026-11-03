# /// script
# dependencies = ["markdown", "weasyprint"]
# ///
from html import escape
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent

HANDOUTS = {
    "pl": [
        ("docs/01_intro/handout.md", "01_wprowadzenie.pdf", "Moduł 1 · Wprowadzenie do ASR"),
        ("docs/02_api_elevenlabs/handout.md", "02_elevenlabs.pdf", "Moduł 2 · ElevenLabs: STT, TTS, API"),
        ("docs/03_colab_intro/handout.md", "03_colab.pdf", "Moduł 3 · Python i Google Colab"),
        ("docs/04_local_whisper/handout.md", "04_whisper.pdf", "Moduł 4 · Modele lokalne: Whisper"),
    ],
    "en": [
        ("docs/01_intro/handout_en.md", "01_intro_en.pdf", "Module 1 · Introduction to ASR"),
        ("docs/02_api_elevenlabs/handout_en.md", "02_elevenlabs_en.pdf", "Module 2 · ElevenLabs: STT, TTS, API"),
        ("docs/03_colab_intro/handout_en.md", "03_colab_en.pdf", "Module 3 · Python and Google Colab"),
        ("docs/04_local_whisper/handout_en.md", "04_whisper_en.pdf", "Module 4 · Local models: Whisper"),
    ],
}

PURPLE = "#2d2a45"
INK = "#191919"
PAPER = "#F8F7F5"
WARM = "#F1EEE9"
GREY = "#5F5F5F"
PINK = "#e75881"
ORANGE = "#f2871e"
YELLOW = "#facf00"

CSS = f"""
@font-face {{ font-family: "Fira Sans"; font-weight: 400; src: url("assets/fonts/FiraSans-Regular.woff2") format("woff2"); }}
@font-face {{ font-family: "Fira Sans"; font-weight: 500; src: url("assets/fonts/FiraSans-Medium.woff2") format("woff2"); }}
@font-face {{ font-family: "Fira Sans"; font-weight: 700; src: url("assets/fonts/FiraSans-Bold.woff2") format("woff2"); }}
@font-face {{ font-family: "M PLUS 1"; font-weight: 400; src: url("assets/fonts/MPLUS1-Regular.woff2") format("woff2"); }}
@font-face {{ font-family: "M PLUS 1"; font-weight: 700; src: url("assets/fonts/MPLUS1-Bold.woff2") format("woff2"); }}
@font-face {{ font-family: "Fira Mono"; font-weight: 400; src: url("assets/fonts/FiraMono-Regular.otf"); }}
@font-face {{ font-family: "Fira Mono"; font-weight: 700; src: url("assets/fonts/FiraMono-Bold.otf"); }}

@page {{
  size: A4;
  margin: 30mm 16mm 18mm 16mm;
  background: {PAPER};
  @bottom-left {{ content: "Brainhack Kraków 2026 · KN AIMed AGH"; font-family: "Fira Sans"; font-size: 8pt; color: {GREY}; }}
  @bottom-right {{ content: counter(page); font-family: "Fira Sans"; font-size: 8pt; color: {GREY}; }}
}}

body {{
  font-family: "M PLUS 1", "DejaVu Sans", sans-serif;
  font-size: 10pt;
  line-height: 1.45;
  color: {INK};
  orphans: 3;
  widows: 3;
}}

.page-header {{
  position: fixed; top: -30mm; left: -16mm; width: 210mm; height: 16mm;
  box-sizing: border-box;
  background: {PURPLE};
  padding: 0 16mm 0 5mm;
  color: #ffffff;
}}
.ph-row {{ display: table; width: 100%; height: 16mm; }}
.ph-row > div {{ display: table-cell; vertical-align: middle; height: 16mm; }}
.ph-logo {{ width: 22mm; }}
.ph-logo img {{ height: 10mm; display: block; }}
.ph-title {{ font-family: "Fira Sans"; font-weight: 700; font-size: 12pt; padding-left: 2mm; }}
.ph-module {{ text-align: right; font-size: 8.5pt; color: {WARM}; }}

.page-rule {{
  position: fixed; top: -14mm; left: -16mm; right: -16mm; height: 1.2mm;
  background: linear-gradient(90deg, {PINK}, {ORANGE}, {YELLOW});
}}

h1 {{ font-family: "Fira Sans"; font-weight: 700; font-size: 20pt; color: {PURPLE}; margin: 0 0 6pt 0; line-height: 1.2; }}
h2 {{ font-family: "Fira Sans"; font-weight: 700; font-size: 14pt; color: {PURPLE}; margin: 12pt 0 5pt 0; border-left: 4px solid {PINK}; padding-left: 7pt; break-after: avoid; }}
h3 {{ font-family: "Fira Sans"; font-weight: 700; font-size: 11pt; color: {PURPLE}; margin: 8pt 0 4pt 0; break-after: avoid; }}
p {{ margin: 0 0 5pt 0; }}
strong {{ color: {INK}; }}

a {{ color: {PURPLE}; text-decoration: underline; text-decoration-color: {PINK}; word-break: break-all; }}

table {{ border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9pt; }}
th, td {{ border: 1px solid #d9d4cc; padding: 3pt 5pt; vertical-align: top; text-align: left; }}
th {{ background: {PURPLE}; color: #ffffff; font-family: "Fira Sans"; font-weight: 500; }}
tr:nth-child(even) td {{ background: {WARM}; }}

blockquote {{ background: {WARM}; border-left: 4px solid {ORANGE}; margin: 8pt 0; padding: 6pt 10pt; break-inside: avoid; }}
blockquote p:last-child {{ margin-bottom: 0; }}

code {{ font-family: "Fira Mono"; font-size: 8.5pt; color: {PURPLE}; }}
pre {{ font-family: "Fira Mono"; font-size: 8.5pt; background: {WARM}; padding: 8pt; white-space: pre-wrap; margin: 8pt 0; break-inside: avoid; }}
pre code {{ color: {INK}; }}

hr {{ border: 0; border-top: 1px solid #d9d4cc; margin: 8pt 0; }}
ul, ol {{ margin: 0 0 6pt 0; padding-left: 16pt; break-inside: avoid; }}
li {{ margin-bottom: 1pt; }}
"""


def page_html(body: str, module_label: str, lang: str = "pl") -> str:
    return f"""<!doctype html>
<html lang="{lang}">
<head><meta charset="utf-8"><style>{CSS}</style></head>
<body>
  <header class="page-header">
    <div class="ph-row">
      <div class="ph-logo"><img src="assets/aimed-logo.png" alt="AIMed"></div>
      <div class="ph-title">Brainhack Kraków 2026</div>
      <div class="ph-module">{escape(module_label)}</div>
    </div>
  </header>
  <div class="page-rule"></div>
  <main>{body}</main>
</body>
</html>"""


def build() -> None:
    for lang, handouts in HANDOUTS.items():
        for source, target, label in handouts:
            text = (ROOT / source).read_text(encoding="utf-8")
            body = markdown.markdown(text, extensions=["tables", "fenced_code"])
            HTML(string=page_html(body, label, lang), base_url=str(ROOT)).write_pdf(ROOT / target)
            print(f"[{lang}] {target} <- {source}")


if __name__ == "__main__":
    build()
