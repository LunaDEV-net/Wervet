#  Copyright (c) 2024 by https://github.com/LunaDEV-net.
#  all rights reserved

import csv
import os


def read_csv_file(path: str, skip_header: bool = True) -> list:
    content: list = []
    with open(path, "r", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=";")
        if True == skip_header:
            # SKIP HEADER (fist line)
            next(reader)

        # for row in reader:
        #     content.append(row)
        content = [row for row in reader] # the same as the for loop above
    return content


def write_dict_to_csv(data_to_write: dict, header_to_write: list, path: str= os.getcwd() + "/data/out.csv"):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header_to_write)
        for key in data_to_write:
            writer.writerows(data_to_write[key])
            # for row in data_to_write[key]:
            #     writer.writerow(row)