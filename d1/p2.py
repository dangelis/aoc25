import math
from enum import StrEnum, auto


class DirEnum(StrEnum):
    L = "L"
    R = "R"


def read_inputs() -> list:
    file_path = 'inputs.txt'
    # file_path = 'test_inputs.txt'

    with open(file_path, 'r') as f:
        lines_list = f.read().splitlines()

    return lines_list


def rotate(dir: DirEnum, clicks: int, current: int) -> int:
    new_pos = None

    # How many times did it loop?
    zero_count = math.floor(clicks / 100)
    print(f"  passed zero {zero_count} times")

    mod_clicks = clicks % 100

    match dir:
        case DirEnum.L:
            new_pos = current - mod_clicks
            print(f"  going left, new_pos: {new_pos}")
            if new_pos < 0:
                if new_pos != 0 and current != 0:
                    zero_count += 1
                new_pos = 100 + new_pos
        case DirEnum.R:
            new_pos = current + mod_clicks
            print(f"  going right, new_pos: {new_pos}")
            if new_pos > 99:
                if new_pos != 0 and new_pos != 100:
                    zero_count += 1
                new_pos = new_pos - 100
        case _:
            raise Exception(f"Unexpected direction {dir}")
    
    #if new_pos == 0:
        #zero_count -= 1  # Don't count it twice if we land on 0
    return new_pos, zero_count


if __name__ == "__main__":
    current_pos = 50
    pass_count = 0
    # Get input
    inputs = read_inputs()
    for input in inputs:
        zero_count = 0
        # parse input to direct and clicks
        direction = DirEnum(input[0:1])
        clicks = int(input[1:])
        print(f"dir: {direction}, clicks: {clicks}, current: {current_pos}")
        current_pos, zero_count = rotate(dir=direction, clicks=clicks, current=current_pos)
        print(f"Now: current pos: {current_pos}, zero_count: {zero_count}")

        if current_pos == 0:
            pass_count += 1

        pass_count = pass_count + zero_count
        print(f"count now: {pass_count}")
            
    
    print(f"pass count: {pass_count}")

# 6707 is too high
