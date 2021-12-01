from typing import Generator, List

EXAMPLE__FILE_NAME = "day-01-example.txt"

INPUT_FILE_NAME = "day-01-input.txt"


def get_input_list(file_name: str) -> List[int]:
    return_list: List[int] = []
    with open(file_name) as input_file:
        for line in input_file:
            return_list.append(int(line))
    return return_list


def construct_list_to_count(file_name: str, block_size: int) -> List[int]:
    depth_readings: List[int] = get_input_list(file_name)
    return [
        sum(entry) for entry in zip(*[depth_readings[i:] for i in range(0, block_size)])
    ]


def count_number_of_increases(file_name: str, block_size: int) -> int:
    list_to_compare: List[int] = construct_list_to_count(file_name, block_size)
    return sum([int(i[1] > i[0]) for i in zip(list_to_compare, list_to_compare[1:])])


print("Example part 1: ", count_number_of_increases(EXAMPLE__FILE_NAME, 1))
print("Result part 1: ", count_number_of_increases(INPUT_FILE_NAME, 1))

print("Example part 2: ", count_number_of_increases(EXAMPLE__FILE_NAME, 3))
print("Result part 2: ", count_number_of_increases(INPUT_FILE_NAME, 3))
