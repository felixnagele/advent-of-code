from pathlib import Path
import sys
from typing import Optional, Any


def read_input(path: Optional[str] = None) -> str:
    if path:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Input file not found: {p}")
        return p.read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    if Path("input.txt").exists():
        return Path("input.txt").read_text(encoding="utf-8")
    if Path("example.txt").exists():
        return Path("example.txt").read_text(encoding="utf-8")
    raise FileNotFoundError(
        "No input found. Provide a file, pipe stdin, or create input.txt/example.txt."
    )


def parse(raw: str) -> Any:
    return raw


def solve(data: Any) -> Any:
    raise NotImplementedError


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        raw = read_input(path)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(2)
    data = parse(raw)
    solve(data)


if __name__ == "__main__":
    main()
