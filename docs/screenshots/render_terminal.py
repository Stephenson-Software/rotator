"""Regenerate the terminal screenshots in this folder.

Each shot runs a real command from the repository root and writes its
actual output, with the command line, into a terminal-style SVG.
Standard library only: python3 docs/screenshots/render_terminal.py
"""
import os
import subprocess
import sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

ROTATE_K = (
    "from rotator import Rotator\n"
    "for k in (2, 6, 8):\n"
    "    xs = [1, 2, 3, 4, 5, 6]\n"
    "    Rotator().rotateRepeat(xs, k)\n"
    "    print('k =', k, '->', xs)"
)

SHOTS = [
    ("demo.svg", "python3 main.py", ["python3", "main.py"]),
    (
        "rotate-repeat.svg",
        'python3 -c "' + ROTATE_K + '"',
        ["python3", "-c", ROTATE_K],
    ),
    ("tests.svg", "python3 -m pytest -q", [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"]),
]

FONT = 14
LINE = 20
CHAR = 8.6
PAD = 16
BAR = 30


def keep(text):
    """Escape text for SVG; non-breaking spaces keep indentation and padding."""
    return escape(text).replace(" ", "\u00a0")


def render(title, display, argv):
    out = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=True).stdout
    out_lines = out.rstrip("\n").split("\n")
    cmd_lines = display.split("\n")
    rows = [("prompt", "$ " + cmd_lines[0])]
    rows += [("prompt", "> " + line) for line in cmd_lines[1:]]
    rows += [("out", line) for line in out_lines]
    width = int(max(len(text) for _, text in rows) * CHAR + 2 * PAD)
    width = max(width, 420)
    height = BAR + PAD + len(rows) * LINE + PAD
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">',
        f'<rect width="{width}" height="{height}" rx="8" fill="#1e1f24"/>',
        f'<rect width="{width}" height="{BAR}" rx="8" fill="#2c2e35"/>',
        f'<rect y="{BAR - 8}" width="{width}" height="8" fill="#2c2e35"/>',
        '<circle cx="18" cy="15" r="5.5" fill="#ff5f57"/>',
        '<circle cx="36" cy="15" r="5.5" fill="#febc2e"/>',
        '<circle cx="54" cy="15" r="5.5" fill="#28c840"/>',
        f'<text x="{width / 2}" y="20" text-anchor="middle" fill="#9aa0ab" '
        f'font-family="ui-sans-serif, system-ui, sans-serif" font-size="12">{escape(title)}</text>',
        f'<g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, \'DejaVu Sans Mono\', monospace" '
        f'font-size="{FONT}">',
    ]
    y = BAR + PAD + FONT
    for kind, text in rows:
        if kind == "prompt":
            sigil, rest = text[:2], text[2:]
            parts.append(
                f'<text x="{PAD}" y="{y}"><tspan fill="#7ee787">{keep(sigil)}</tspan>'
                f'<tspan fill="#e6edf3">{keep(rest)}</tspan></text>'
            )
        else:
            parts.append(f'<text x="{PAD}" y="{y}" fill="#c9d1d9">{keep(text)}</text>')
        y += LINE
    parts.append("</g></svg>")
    return "\n".join(parts) + "\n"


def main():
    for name, display, argv in SHOTS:
        title = "rotator: " + display.split("\n")[0].split('"')[0].strip()
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(render(title, display, argv))
        print("wrote", os.path.join("docs", "screenshots", name))


if __name__ == "__main__":
    main()
