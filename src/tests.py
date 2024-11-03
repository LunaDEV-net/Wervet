import sys

from configuration import Default, configuration


def check_data(data_in: list, const_data: Default):
    # Test 1
    if len(data_in) == 0:
        sys.exit("Test 1 failed: No data found")
    for line_num, line in enumerate(data_in):
        # # Test 2
        # if len(data_in[line_num]) != const_data.number_of_columns:
        #     sys.exit(f"Test 2 failed: Data format of CSV file changed and is not supported! \n {len(data_in[line_num])} in line {line_num} != {const_data.number_of_columns}")
        # Hat immer Fehler bei von mir bearbeiten CSV Files gemacht
        # Test 3
        for i in const_data.should_not_be_empty_columns:
            if line[i] == "":
                sys.exit(f"Test 3 failed: Empty column found in line {line_num}")
        # Test 4
        for columns in line:
            if any(char in columns for char in const_data.disallowed_characters):
                sys.exit(f"Test 4 failed: Disallowed character ({const_data.disallowed_characters}) found in line {line_num}")
        # Test 5
        if line[const_data.indikator] not in const_data.indexe_indikatoren:
            sys.exit(f"Test 5 failed: Indikator not found in indexe_indikatoren in line {line_num}")



    pass
if __name__ == '__main__':
    check_data([["a","d","s","f","g","h","h","j","k","l","ö","","",]], configuration)
