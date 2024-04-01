import csv


def write_csv(path, dict, write_header=False):
    with open(path, 'a', newline='\n', encoding='utf-8') as file:
        writer = csv.DictWriter(file, dict.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(dict)
