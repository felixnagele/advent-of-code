import sys
from pathlib import Path


def get_input(caller_file: str) -> list[str]:
    """
    Reads input.txt or falls back to example.txt in the caller's directory.
    Returns a list of stripped lines.
    """

    folder: Path = Path(caller_file).parent

    input_file: Path = folder / "input.txt"
    example_file: Path = folder / "example.txt"

    target: Path

    if input_file.exists():
        target = input_file
    elif example_file.exists():
        print(f"INFO: input.txt not found. Using {example_file.name} as fallback.")
        target = example_file
    else:
        print(f"ERROR: Neither input.txt nor example.txt found in {folder}")
        sys.exit(1)

    return target.read_text().splitlines()
