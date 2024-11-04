#  Copyright (c) 2024 by https://github.com/LunaDEV-net.
#  all rights reserved

import sys
from errors import EmptyDataError, EmptyColumnError
from configuration import Default, configuration as config


def length_of_data(data_in: list):
    """fails if the data dir is empty"""
    if len(data_in) == 0:
        raise EmptyDataError

def empty_columns(data_in: list):
    for line_num, line in enumerate(data_in):
        for i in config.should_not_be_empty_columns:
            if line[i] == "":
                raise EmptyColumnError(line_num)

def check_data(data_in: list):
    length_of_data(data_in)
    empty_columns(data_in)
    for line_num, line in enumerate(data_in):
        for columns in line:
            if any(char in columns for char in const_data.disallowed_characters):
                sys.exit(f"Test 4 failed: Disallowed character ({const_data.disallowed_characters}) found in line {line_num}")
        if line[const_data.indikator] not in const_data.indexe_indikatoren:
            sys.exit(f"Test 5 failed: Indikator not found in indexe_indikatoren in line {line_num}")



    pass
if __name__ == '__main__':
    empty_columns([["" for i in range(20)] for j in range(20)])
