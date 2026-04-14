# advent-of-code 🎄

My [Advent of Code](https://adventofcode.com/) solutions.

## 🛠 Requirements

- Python
- Package manager: uv

## 🚀 Quick Start

### Step 1: Clone the repo

```bash
git clone https://github.com/felixnagele/advent-of-code.git
cd advent-of-code
```

### Step 2: Install dependencies

```bash
uv sync
```

## 📖 Usage

### Run a solution for a specific year and day

```bash
uv run python -m [year].day[01-25].solution
```

Example for 2015 Day 1:

```bash
uv run python -m 2015.day01.solution
```

Note on input: The solutions expect an `input.txt` file in the same directory as the solution file.

Quick test: Every folder already has an `example.txt`, so you can run the code immediately to see it in action.

## 📝 Note

This is a personal repository for tracking my progress and archiving my solutions. It is not intended for external contributions.
