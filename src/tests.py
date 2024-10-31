import sys

from src.const import Default


def check_data(data_in: list, const_data: Default):
    # Test 1
    if len(data_in) == 0:
        sys.exit("Test 1 failed: No data found")
    for line_num in range(len(data_in)):
        # Test 2
        if len(data_in[line_num]) != const_data.number_of_colums:
            sys.exit(f"Test 2 failed: Data format of CSV file changed and is not supported! \n {len(data_in[line_num])} in line {line_num} != {const_data.number_of_colums}")
        # Test 3
        for i in const_data.should_not_be_empty_colums:
            if data_in[line_num][i] == "":
                sys.exit(f"Test 3 failed: Empty column found in line {line_num}")
        for collumn in data_in[line_num]:
            if any(char in collumn for char in const_data.disallowed_characters):
                sys.exit(f"Test 4 failed: Disallowed character ({const_data.disallowed_characters}) found in line {line_num}")



    pass
if __name__ == '__main__':
    check_data([["a","d","s","f","g","h","h","j","k","l","ö","","",]], Default())