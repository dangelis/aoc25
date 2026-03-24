# Find invalid IDs in provided id ranges
# Invalid IDs have repeating digits

# Read in input

# Split input into ranges

# For each range
    # Create range and loop over it
        # For each number in range,
            # stringify it
            # Capture the characters Left to Right for half the length
            # See if the second half matches and save it off

# Add all the bad ids


def get_ranges(file_name) -> list[str]:
    with open(file_name) as file:
        lines = file.read().replace('\n', '').split(",")

    return lines



if __name__ == "__main__":
    #ranges = get_ranges("test_input.txt")
    ranges = get_ranges("input.txt")
    #print(f"lines: {ranges}")

    matches: list[int] = []
    for r in ranges:
        r_item = r.split('-')
        for x in range(int(r_item[0]), int(r_item[1]) + 1):
            x_str = str(x)
            half_idx = len(x_str) / 2
            half_idx_i = int(half_idx)
            #print(f"x_str: {x_str}, len {len(x_str)}, half_idx: {half_idx_i}")
            
            first = x_str[half_idx_i:]
            second = x_str[:half_idx_i]
            if first == second:
                print(f"    Found match: {x_str}")
                matches.append(x)

    total = sum(matches)
    print(f"total: {total}")
    

