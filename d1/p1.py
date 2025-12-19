
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
    print(f"rotate with dir: {dir}, clicks: {clicks}, current: {current}")
    new_pos = None

    mod_clicks = clicks % 100

    match dir:
        case DirEnum.L:
            new_pos = current - mod_clicks
            if new_pos < 0:
                new_pos = 100 + new_pos
        case DirEnum.R:
            new_pos = current + mod_clicks
            if new_pos > 99:
                new_pos = new_pos - 100
        case _:
            raise Exception(f"Unexpected direction {dir}")
    
    return new_pos


if __name__ == "__main__":
    current_pos = 50
    pass_count = 0
    # Get input
    inputs = read_inputs()
    for input in inputs:
        # parse input to direct and clicks
        direction = DirEnum(input[0:1])
        clicks = int(input[1:])
        print(f"dir: {direction}, clicks: {clicks}")
        current_pos = rotate(dir=direction, clicks=clicks, current=current_pos)
        print(f"current pos: {current_pos}")
        if current_pos == 0:
            pass_count = pass_count + 1
            
    
    print(f"pass count: {pass_count}")


# 234 too low
# 1081 is it