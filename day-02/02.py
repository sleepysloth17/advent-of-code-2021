from typing import Generator, List, Tuple

EXAMPLE_FILE_NAME: str = "day-02-example.txt"

INPUT_FILE_NAME: str = "day-02-input.txt"


class Position:
    def __init__(self):
        self.horizontal: int = 0
        self.depth: int = 0
        self.aim: int = 0

    def apply_command(self, command: Tuple[str, int]) -> None:
        match command:
            case "forward", i:
                self.horizontal += i
                self.depth += self.aim * i
            case "down", i:
                self.aim += i
            case "up", i:
                self.aim -= i

    def multiply(self) -> str:
        return self.horizontal * self.depth


def get_input_list(file_name: str) -> Generator[Tuple[str, int], None, None]:
    with open(file_name) as input_file:
        for line in input_file:
            split_line: List[str] = line.split()
            yield (split_line[0], int(split_line[1]))


def run(file_name: str) -> int:
    position: Position = Position()
    for command in get_input_list(file_name):
        position.apply_command(command)
    return position.multiply()


print("Example part 1: ", run(EXAMPLE_FILE_NAME))
print("Input part 1: ", run(INPUT_FILE_NAME))
