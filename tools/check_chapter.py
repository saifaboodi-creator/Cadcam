"""Check a chapter's citations, references and UNVERIFIED count.

Usage:
  python3 -I tools/check_chapter.py chapters/NN-slug.md [...]   # check given chapters
  python3 -I tools/check_chapter.py --all                       # all chapters + PROGRESS.md counts
  python3 -I tools/check_chapter.py --hook                      # Claude Code hook (reads JSON on stdin)

Exit 0 = pass. Exit 2 = fail (problems on stderr) — exit code 2 is what sends
Claude back to fix the problem instead of marking the task done.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CITE = re.compile(r'\[(\d+(?:[–,]\d+)*)\]')
REF = re.compile(r'^(\d+)\. ', re.M)


def expand(g):
    out = []
    for part in g.split(','):
        if '–' in part:
            a, b = map(int, part.split('–'))
            out += range(a, b + 1)
        else:
            out.append(int(part))
    return out


def check(path):
    """Return (problems, unverified_count) for one chapter file."""
    name = os.path.basename(path)
    s = open(path, encoding='utf-8').read()
    if '## References\n' not in s:
        return [f"{name}: no '## References' heading"], 0
    body, refs = s.split('## References\n', 1)
    problems = []

    order = []
    for m in CITE.finditer(body):
        for n in expand(m.group(1)):
            if n not in order:
                order.append(n)
    listed = [int(n) for n in REF.findall(refs)]

    missing = sorted(set(order) - set(listed))
    unused = sorted(set(listed) - set(order))
    if missing:
        problems.append(f"{name}: cited but not in reference list: {missing}")
    if unused:
        problems.append(f"{name}: in reference list but never cited: {unused}")
    if len(listed) != len(set(listed)):
        problems.append(f"{name}: duplicate reference numbers in the list")
    if listed != sorted(listed) or (listed and listed != list(range(1, len(listed) + 1))):
        problems.append(f"{name}: reference list is not numbered 1..N in order")
    if order != list(range(1, len(order) + 1)):
        problems.append(f"{name}: citations are not in order of first appearance — "
                        f"run: python3 -I tools/renum.py chapters/{name}")
    return problems, body.count('UNVERIFIED')


def progress_counts():
    """Chapter number -> UNVERIFIED count as recorded in PROGRESS.md."""
    out = {}
    p = os.path.join(ROOT, 'PROGRESS.md')
    for line in open(p, encoding='utf-8'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) >= 6 and cells[0].isdigit() and cells[5].isdigit():
            out[int(cells[0])] = int(cells[5])
    return out


def chapter_files():
    return sorted(f for f in glob.glob(os.path.join(ROOT, 'chapters', '[0-9][0-9]-*.md'))
                  if not f.endswith('.notes.md'))


def is_chapter(path):
    return bool(re.search(r'chapters/\d\d-[^/]*\.md$', path)) and not path.endswith('.notes.md')


def check_all():
    problems = []
    recorded = progress_counts()
    for f in chapter_files():
        p, unv = check(f)
        problems += p
        ch = int(os.path.basename(f)[:2])
        if ch in recorded and recorded[ch] != unv:
            problems.append(f"{os.path.basename(f)}: {unv} UNVERIFIED marks in the text, "
                            f"but PROGRESS.md records {recorded[ch]} — update PROGRESS.md")
    return problems


def main(argv):
    if argv[:1] == ['--hook']:
        data = json.load(sys.stdin)
        if data.get('hook_event_name') == 'Stop':
            if data.get('stop_hook_active'):
                return 0  # already sent back once; don't loop forever
            problems = check_all()
        else:
            path = (data.get('tool_input') or {}).get('file_path', '')
            if not is_chapter(path):
                return 0
            problems, _ = check(path)
    elif argv[:1] == ['--all']:
        problems = check_all()
    else:
        problems = [p for f in argv for p in check(f)[0]]

    if problems:
        print("Chapter check FAILED:\n- " + "\n- ".join(problems), file=sys.stderr)
        return 2
    print("Chapter check passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
