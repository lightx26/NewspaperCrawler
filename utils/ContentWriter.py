import csv


# def write(path, content):
#     with open(path, 'a', encoding='utf-8') as file:
#         file.write(content)


def write_csv(path, dict):
    with open(path, 'a', newline='\n', encoding='utf-8') as file:
        writer = csv.DictWriter(file, dict.keys())
        # writer.writeheader()
        writer.writerow(dict)
