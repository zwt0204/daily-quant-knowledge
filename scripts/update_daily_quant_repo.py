#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

ROOT = Path('/root/.openclaw/workspace/daily-quant-knowledge')
INDEX = ROOT / 'index.md'


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'untitled'


def ensure_index():
    if not INDEX.exists():
        INDEX.write_text(
            '# Daily Quant Knowledge Index\n\n'
            '## Repo Structure\n\n'
            '- `notes/YYYY/`: daily study notes\n'
            '- `code/`: runnable example scripts\n'
            '- `assets/`: charts/images\n\n'
            '## Progress\n\n',
            encoding='utf-8'
        )


def append_index(day: int, note_rel: str, title: str):
    ensure_index()
    line = f'- [Day {day} - {title}]({note_rel})\n'
    content = INDEX.read_text(encoding='utf-8')
    if line not in content:
        if not content.endswith('\n'):
            content += '\n'
        content += line
        INDEX.write_text(content, encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--day', type=int, required=True)
    ap.add_argument('--title', required=True)
    ap.add_argument('--date', default=datetime.now().strftime('%Y-%m-%d'))
    ap.add_argument('--note', required=True)
    ap.add_argument('--code', default='')
    args = ap.parse_args()

    year = args.date[:4]
    title_slug = slugify(args.title)
    notes_dir = ROOT / 'notes' / year
    code_dir = ROOT / 'code'
    notes_dir.mkdir(parents=True, exist_ok=True)
    code_dir.mkdir(parents=True, exist_ok=True)

    note_name = f"{args.date}-day{args.day:02d}-{title_slug}.md"
    note_path = notes_dir / note_name
    note_path.write_text(args.note.rstrip() + '\n', encoding='utf-8')

    if args.code.strip():
        code_name = f"day{args.day:02d}_{title_slug}.py"
        (code_dir / code_name).write_text(args.code.rstrip() + '\n', encoding='utf-8')

    append_index(args.day, f'notes/{year}/{note_name}', args.title)
    print(note_path)


if __name__ == '__main__':
    main()
