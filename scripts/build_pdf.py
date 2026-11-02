# /// script
# dependencies = ["markdown", "weasyprint"]
# ///
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent

HANDOUTS = {
    "docs/01_intro/handout.md": "01_wprowadzenie.pdf",
    "docs/02_api_elevenlabs/handout.md": "02_elevenlabs.pdf",
    "docs/03_colab_intro/handout.md": "03_colab.pdf",
    "docs/04_local_whisper/handout.md": "04_whisper.pdf",
}

CSS = """
@page {
  size: A4;
  margin: 18mm 16mm;
  @bottom-right { content: counter(page); font-size: 9pt; color: #666; }
}
body { font-family: "DejaVu Sans", sans-serif; font-size: 10.5pt; line-height: 1.45; color: #222; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4pt; }
h2 { font-size: 14pt; margin-top: 16pt; color: #1a4d7a; }
h3 { font-size: 12pt; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9.5pt; }
th, td { border: 1px solid #999; padding: 4pt 6pt; vertical-align: top; }
th { background: #eee; }
code, pre { font-family: "DejaVu Sans Mono", monospace; font-size: 8.5pt; }
pre { background: #f5f5f5; border: 1px solid #ddd; padding: 6pt; white-space: pre-wrap; }
blockquote { border-left: 3px solid #1a4d7a; margin: 8pt 0; padding: 2pt 10pt; background: #f3f7fb; }
hr { border: 0; border-top: 1px solid #ccc; margin: 12pt 0; }
a { color: #1a4d7a; word-break: break-all; }
"""


def build() -> None:
    for source, target in HANDOUTS.items():
        text = (ROOT / source).read_text(encoding="utf-8")
        body = markdown.markdown(text, extensions=["tables", "fenced_code"])
        html = (
            '<!doctype html><html lang="pl"><head><meta charset="utf-8">'
            f"<style>{CSS}</style></head><body>{body}</body></html>"
        )
        HTML(string=html).write_pdf(ROOT / target)
        print(f"{target} <- {source}")


if __name__ == "__main__":
    build()
