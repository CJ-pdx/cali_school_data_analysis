from pathlib import Path
import re
import numpy
import pandas

data_folder = Path("../CaliSchoolData/data/SuspensionData/rawTextData/")

file_to_open = data_folder / 'susp1112.txt'
file = open(file_to_open, 'rt')
textData = file.read()
file.close()

data_list = textData.splitlines(keepends=True)

print(data_list[5])
print(data_list[6])

data_list = [','.join(line.split()) for line in data_list]

print(data_list[5])
print(data_list[6])