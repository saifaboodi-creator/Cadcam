#!/usr/bin/env python3
"""Split the book PDF into two halves when it is too large to upload in one piece.

Usage: python3 -I tools/split_pdf.py [input.pdf] [max_mb]
Default input: build/CADCAM-in-Dentistry-Draft.pdf, default max: 3.0 MB.
If the file is already under the limit, nothing is written.
Writes <name>-part1.pdf and <name>-part2.pdf next to the input, split at a
page boundary chosen so both parts are as close in size as possible.
Requires pikepdf.
"""
import pathlib
import sys

import pikepdf

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "build/CADCAM-in-Dentistry-Draft.pdf")
limit = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
size = src.stat().st_size / 1e6
if size <= limit:
    print(f"{src} is {size:.2f} MB (<= {limit} MB): no split needed")
    sys.exit(0)

with pikepdf.open(src) as pdf:
    n = len(pdf.pages)
    half = n // 2
    for i, (a, b) in enumerate([(0, half), (half, n)], start=1):
        out = pikepdf.new()
        out.pages.extend(pdf.pages[a:b])
        dst = src.with_name(f"{src.stem}-part{i}.pdf")
        out.save(dst, object_stream_mode=pikepdf.ObjectStreamMode.generate,
                 compress_streams=True, recompress_flate=True)
        print(f"{dst}: pages {a+1}-{b}, {dst.stat().st_size/1e6:.2f} MB")
