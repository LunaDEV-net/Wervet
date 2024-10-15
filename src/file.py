import csv
import os


def read_csv_file(path: str, skip_header: bool = True) -> list:
    content: list = []
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=";")
        if skip_header == True:
            # SKIP HEADER (fist line)
            next(reader)

        # for row in reader:
        #     content.append(row)
        content = [row for row in reader] # the same as the for loop above
    return content


def write_dict_to_csv(data_to_write: dict, path: str= os.getcwd() + "/data/out.csv"):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        for key in data_to_write:
            writer.writerows(data_to_write[key])
            # for row in data_to_write[key]:
            #     writer.writerow(row)

