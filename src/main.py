import os
import cli, data, file
from src.data import process_data


def main(path_in: str, path_out: str):
    file_contents = file.read_csv_file(path_in)
    processed_data: dict = process_data(file_contents)
    file.write_dict_to_csv(processed_data, path_out)


if __name__ == '__main__':
    main(os.getcwd()+"/data/in.csv", os.getcwd()+"/data/out.csv")
