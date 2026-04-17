from utils import io


def parse(raw_data: list[str]) -> list[str]:
    data: str = "".join(raw_data)
    out: list[str] = []

    for char in data:
        out.append(char)

    return out


def switch_floor(instruction: str, current_floor: int) -> int:
    if instruction == "(":
        current_floor += 1
    elif instruction == ")":
        current_floor -= 1
    else:
        raise ValueError("Unknown instruction")

    return current_floor


def solve_part1(data: list[str]) -> int:
    current_floor: int = 0

    for char in data:
        current_floor = switch_floor(instruction=char, current_floor=current_floor)

    return current_floor


def solve_part2(data: list[str]) -> int:
    current_floor: int = 0
    counter_floor: int = 0

    for char in data:
        counter_floor += 1
        current_floor = switch_floor(instruction=char, current_floor=current_floor)

        if current_floor <= -1:
            break

    return counter_floor


if __name__ == "__main__":
    raw = io.get_input(__file__)

    parsed_data = parse(raw_data=raw)

    part1 = solve_part1(parsed_data)
    part2 = solve_part2(parsed_data)

    print("=== Advent of Code ===")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
