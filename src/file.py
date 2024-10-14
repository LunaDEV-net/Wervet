import csv
import os


def read_csv_file(path: str):
    content: list = []
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=";")
        # SKIP HEADER (fist line)
        next(reader)

        for row in reader:
            content.append(row)
    return content


def write_dict_to_csv(data_to_write: dict, path: str= os.getcwd() + "/data/out.csv"):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        for key in data_to_write:
            writer.writerows(data_to_write[key])
            # for row in data_to_write[key]:
            #     writer.writerow(row)

