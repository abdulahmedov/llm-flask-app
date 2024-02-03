from typing import List
import csv


def read_datafile(filename: str) -> List[str]:
  """Reads csv file with python span list and text."""
  data = []
  with open(filename, encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            data.append(row['***'])
  return data
