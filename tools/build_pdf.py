#!/usr/bin/env python3
"""Build the book PDF from chapters/*.md (notes files excluded).

Usage (from the repository root):
    python3 -I tools/build_pdf.py
Output: build/CADCAM-in-Dentistry-Draft.pdf (and build/book.html)

Requires pandoc and Playwright with Chromium (both preinstalled in the
cloud environment).
"""
import datetime
import html
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAPTERS = sorted(p for p in (ROOT / "chapters").glob("[0-9][0-9]-*.md")
                  if not p.name.endswith(".notes.md"))
OUT = ROOT / "build"
OUT.mkdir(exist_ok=True)

TITLE = "CAD/CAM in Dentistry"
SUBTITLE = "From Scan to Restoration"

PARTS = {
    1: ("Part I", "Foundations"),
    4: ("Part II", "Data Acquisition"),
    7: ("Part III", "Computer-Aided Design"),
    10: ("Part IV", "Computer-Aided Manufacturing"),
    13: ("Part V", "Materials for CAD/CAM"),
    16: ("Part VI", "Clinical Applications"),
    20: ("Part VII", "Practice and the Future"),
}

CSS = """
@page { size: A4; margin: 22mm 20mm 22mm 22mm; }
:root { --ink:#1b1f24; --muted:#5b6470; --accent:#1f5f8b; --rule:#cfd6de; --box:#f3f7fa; }
html { font-family: 'Bitstream Charter','Caladea','DejaVu Serif',serif; font-size: 10.5pt; color: var(--ink); }
body { margin: 0; line-height: 1.45; }
h1, h2, h3, h4 { font-family: 'Inter','Carlito','DejaVu Sans',sans-serif; color: var(--ink); line-height: 1.2; }
h1 { font-size: 22pt; font-weight: 700; margin: 0 0 14pt; padding-bottom: 8pt; border-bottom: 2pt solid var(--accent); }
h2 { font-size: 13.5pt; font-weight: 650; color: var(--accent); margin: 18pt 0 6pt; break-after: avoid; }
h3 { font-size: 11.5pt; font-weight: 600; margin: 12pt 0 4pt; break-after: avoid; }
h4 { font-size: 10.5pt; font-weight: 600; margin: 10pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 7pt; padding-left: 18pt; }
li { margin: 0 0 2.5pt; }
strong { font-weight: 700; }
hr { border: 0; border-top: 0.6pt solid var(--rule); margin: 12pt 0; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 8.6pt; line-height: 1.3;
        font-family: 'Inter','Carlito','DejaVu Sans',sans-serif; break-inside: auto; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
th { background: #e6eef5; text-align: left; font-weight: 600; }
th, td { border: 0.5pt solid var(--rule); padding: 3pt 5pt; vertical-align: top; }
blockquote { margin: 8pt 0 10pt; padding: 7pt 10pt; background: var(--box); border-left: 3pt solid var(--accent);
             break-inside: avoid; font-size: 9.8pt; }
blockquote p { margin: 0; text-align: left; }
code { font-family: 'JetBrains Mono','DejaVu Sans Mono',monospace; font-size: 9pt; }
a { color: var(--accent); text-decoration: none; }
.chapter { break-before: page; }
figure { margin: 10pt 0 12pt; break-inside: avoid; text-align: center; }
figure img { max-width: 100%; max-height: 150mm; height: auto; display: block; margin: 0 auto 5pt; }
figcaption { font-size: 9pt; color: #3a3f45; text-align: left; line-height: 1.35; }
p.cap { break-after: avoid; page-break-after: avoid; margin-bottom: 3pt; text-align: left; }
p.cap + table tr:first-child, p.cap + table thead { break-before: avoid; }
.chapter h2#references + ol, .refs { font-size: 8.8pt; }
.refs p, .refs li { text-align: left; hyphens: none; word-break: break-word; }
.vnote { margin: 4pt 0 10pt; padding: 5pt 7pt 1pt; border: 0.8pt solid #d9a400; border-left: 3pt solid #d9a400;
         background: #fffaf0; break-inside: avoid; }
.keep { break-inside: avoid; }
.vnote.major { border-color: #b3261e; background: #fdf1f0; }
.vnote p { margin: 0 0 3pt; font-size: 8.8pt; text-align: left; font-family: 'Inter','Carlito','DejaVu Sans',sans-serif; }
.vnote table { margin: 0 0 4pt; font-size: 8pt; background: #fff; }
.vnote.major p strong, .vnote.major td strong { color: #b3261e; }
.vnote.minor p strong, .vnote.minor td strong { color: #7a4b00; }
.unv { background: #fff1c7; color: #7a4b00; font-weight: 700; padding: 0 2pt; border-radius: 2pt; white-space: nowrap; }
/* title page */
.titlepage { height: 245mm; display: flex; flex-direction: column; justify-content: center; break-after: page; }
.titlepage .t1 { font-family: 'Inter',sans-serif; font-size: 34pt; font-weight: 800; line-height: 1.1; margin: 0; }
.titlepage .t2 { font-family: 'Inter',sans-serif; font-size: 18pt; font-weight: 400; color: var(--accent); margin: 8pt 0 30pt; }
.titlepage .meta { font-size: 10.5pt; color: var(--muted); border-top: 1pt solid var(--rule); padding-top: 10pt; max-width: 120mm; }
.titlepage .meta p { text-align: left; margin: 0 0 4pt; }
/* part pages */
.part { break-before: page; break-after: page; height: 245mm; display: flex; flex-direction: column; justify-content: center; }
.part .pn { font-family: 'Inter',sans-serif; font-size: 13pt; letter-spacing: 3pt; text-transform: uppercase; color: var(--accent); margin: 0; }
.part .pt { font-family: 'Inter',sans-serif; font-size: 28pt; font-weight: 700; margin: 6pt 0 16pt; }
.part ul { list-style: none; padding: 0; font-size: 11pt; color: var(--muted); }
/* contents */
.toc { break-after: page; }
.toc h1 { border-bottom: 2pt solid var(--accent); }
.toc .tp { font-family: 'Inter',sans-serif; font-weight: 700; font-size: 10pt; color: var(--accent);
           text-transform: uppercase; letter-spacing: 1.2pt; margin: 12pt 0 3pt; }
.toc ol { list-style: none; padding: 0; margin: 0; }
.toc li { margin: 0 0 3pt; font-size: 11pt; }
.toc li a { color: var(--ink); }
.toc .num { display: inline-block; width: 24pt; color: var(--muted); }
.notice { font-size: 9.5pt; color: var(--muted); margin-top: 18pt; }
"""


def keep_with_previous(out):
    """Wrap each verification note with the block just before it (paragraph, list, table or figure),
    so the note is printed on the same page as the text it refers to."""
    pieces, pos = [], 0
    for m in re.finditer(r'<div class="vnote [a-z]+">.*?</table></div>', out, flags=re.S):
        before = out[pos:m.start()].rstrip()
        tag = re.search(r'</(p|ul|ol|table|figure)>$', before)
        if not tag:
            pieces.append(out[pos:m.end()]); pos = m.end(); continue
        name = tag.group(1)
        start = max(before.rfind(f'<{name}>'), before.rfind(f'<{name} '))
        if name in ('ul', 'ol'):  # include a lead-in paragraph that ends with a colon
            lead = re.search(r'<p>(?:(?!<p[ >]).)*?:(?:</strong>)?(?:\s*<span class="unv">\[UNVERIFIED\]</span>)?:?</p>\s*$',
                             before[:start], flags=re.S)
            if lead: start = lead.start()
        if name == 'table':
            cap = re.search(r'<p class="cap">(?:(?!<p[ >]).)*?</p>\s*$', before[:start], flags=re.S)
            if cap: start = cap.start()
        pieces.append(before[:start])
        pieces.append(f'<div class="keep">{before[start:]}\n{m.group(0)}</div>')
        pos = m.end()
    pieces.append(out[pos:])
    return ''.join(pieces)


def chapter_html(path):
    out = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none", str(path)],
        check=True, capture_output=True, text=True).stdout
    # Highlight UNVERIFIED markers so the author can find them.
    out = re.sub(r"<strong>\[UNVERIFIED\]</strong>|\[UNVERIFIED\]",
                 '<span class="unv">[UNVERIFIED]</span>', out)
    # Turn "image paragraph + **Figure N.M** caption" into a <figure> that stays on one page.
    out = re.sub(r'<p>(<img [^>]*>)</p>\s*<p>(<strong>Figure \d+\.\d+</strong>.*?)</p>',
                 r'<figure>\1<figcaption>\2</figcaption></figure>', out, flags=re.S)
    # Keep table captions ("Table N.N ...") on the same page as their table.
    out = re.sub(r'<p>(<strong>Table \d+\.\d+</strong>.*?)</p>\s*(<table>)',
                 r'<p class="cap">\1</p>\n\2', out, flags=re.S)
    # Verification notes (author request 2026-11-25): keep each note box with its table, on the same page.
    out = re.sub(r'<p>(<strong>Verification note — (Major|Minor) conflict\.</strong>.*?)</p>\s*(<table>.*?</table>)',
                 lambda m: f'<div class="vnote {m.group(2).lower()}"><p>{m.group(1)}</p>{m.group(3)}</div>',
                 out, flags=re.S)
    out = keep_with_previous(out)
    # Wrap the reference list for smaller type.
    out = re.sub(r'(<h2 id="references">References</h2>\s*)(<ol>.*?</ol>)',
                 r'\1<div class="refs">\2</div>', out, flags=re.S)
    return out


def main():
    items = []
    for path in CHAPTERS:
        num = int(path.name[:2])
        first = path.read_text(encoding="utf-8").splitlines()[0]
        title = re.sub(r"^#\s*Chapter\s+\d+\.\s*", "", first).strip()
        items.append((num, title, path))

    today = datetime.date.today().strftime("%d %B %Y")
    parts_html, toc = [], []
    for num, title, path in items:
        if num in PARTS:
            pn, pt = PARTS[num]
            toc.append(f'<div class="tp">{pn} — {html.escape(pt)}</div><ol>')
        toc.append(f'<li><a href="#ch{num}"><span class="num">{num}</span>{html.escape(title)}</a></li>')
        nxt = num + 1
        if nxt in PARTS or nxt > items[-1][0]:
            toc.append("</ol>")

    for num, title, path in items:
        if num in PARTS:
            pn, pt = PARTS[num]
            members = [f"Chapter {n}. {html.escape(t)}" for n, t, _ in items
                       if n >= num and (n < min([k for k in PARTS if k > num] + [999]))]
            parts_html.append(
                f'<section class="part"><p class="pn">{pn}</p><p class="pt">{html.escape(pt)}</p>'
                f'<ul>{"".join(f"<li>{m}</li>" for m in members)}</ul></section>')
        parts_html.append(f'<section class="chapter" id="ch{num}">{chapter_html(path)}</section>')

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{TITLE}: {SUBTITLE}</title><style>{CSS}</style></head><body>
<section class="titlepage">
  <p class="t1">{TITLE}</p><p class="t2">{SUBTITLE}</p>
  <div class="meta">
    <p><strong>Draft manuscript — for author review</strong></p>
    <p>Compiled {today} · {len(items)} chapters</p>
    <p>References in Vancouver style, verified against PubMed. Statements marked
    <span class="unv">[UNVERIFIED]</span> await confirmation; see the chapter notes files.</p>
  </div>
</section>
<section class="toc"><h1>Contents</h1>{''.join(toc)}
<p class="notice">Review notes for each chapter are kept separately in <code>chapters/NN-*.notes.md</code>.</p></section>
{''.join(parts_html)}
</body></html>"""
    html_path = OUT / "book.html"
    html_path.write_text(doc, encoding="utf-8")

    pdf_path = OUT / "CADCAM-in-Dentistry-Draft.pdf"
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{html_path}', {{ waitUntil: 'load' }});
  const opts = {{
    path: '{pdf_path}', format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<div style="font-size:7.5pt;width:100%;padding:0 20mm 0 22mm;color:#7a8490;font-family:Inter,sans-serif;text-align:right;">{TITLE}: {SUBTITLE} — Draft</div>',
    footerTemplate: '<div style="font-size:8pt;width:100%;text-align:center;color:#7a8490;font-family:Inter,sans-serif;"><span class="pageNumber"></span></div>',
    margin: {{ top: '22mm', bottom: '22mm', left: '22mm', right: '20mm' }},
  }};
  try {{ await p.pdf({{ ...opts, outline: true, tagged: true }}); }}
  catch (e) {{ await p.pdf(opts); }}
  await b.close();
}})();
"""
    subprocess.run(["node", "-e", js], check=True, cwd=str(OUT))
    compress(pdf_path)
    print(pdf_path)


def compress(pdf_path):
    """Lossless size reduction (object streams + recompressed streams).

    Keeps every page, font, vector figure and text identical; needed because
    connector uploads (e.g. Google Drive) are limited to about 3.1 MB per file.
    Requires pikepdf (pip install pikepdf); skipped with a warning if missing.
    """
    try:
        import pikepdf
    except ImportError:
        print("WARNING: pikepdf not installed; PDF left uncompressed (pip install pikepdf)")
        return
    tmp = pdf_path.with_suffix(".tmp.pdf")
    with pikepdf.open(pdf_path) as pdf:
        pdf.save(tmp, object_stream_mode=pikepdf.ObjectStreamMode.generate,
                 compress_streams=True, recompress_flate=True)
    before, after = pdf_path.stat().st_size, tmp.stat().st_size
    tmp.replace(pdf_path)
    print(f"compressed: {before/1e6:.2f} MB -> {after/1e6:.2f} MB")


if __name__ == "__main__":
    main()
