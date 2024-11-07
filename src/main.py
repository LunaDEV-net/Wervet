#  Copyright (c) 2024 by https://github.com/LunaDEV-net.
#  all rights reserved

import argparse
import pathlib
import file
import configuration
from data import process_data

__version__ = "2024-11-1_v1.9"

def main(path_in: pathlib.Path, path_out: pathlib.Path):
    file_contents = file.read_csv_file(path_in)
    print("Read file")
    config = configuration.configuration
    print("Got ")
    processed_data: dict = process_data(file_contents)
    file.write_dict_to_csv(processed_data, config.header, path_out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A local python tool to turn raw data from the Aktion Saubere Hände into an excel friendly dataset.",
        epilog=r'https://github.com/LunaDEV-net/WebKess  Support: Contact me personally or write a [Github Issue](https://github.com/LunaDEV-net/WebKess/issues)'
    )
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('path_in', type=pathlib.Path, help='Input CSV file path')
    parser.add_argument('path_out', type=pathlib.Path, help='Output CSV file path')

    try:
        print("Starting...")
        args = parser.parse_args()
        main(args.path_in, args.path_out)
        print(f"Done. Written to {args.path_out}")
    except Exception as e:
        print(e)
        print("\nPlease use --help for more information.")