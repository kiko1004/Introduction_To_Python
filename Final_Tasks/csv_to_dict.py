# reads a CSV file and converts it to a dictionary
import csv

def csv_to_dict(file_name):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            key = row.pop('id')
            data[key] = row
        return data
