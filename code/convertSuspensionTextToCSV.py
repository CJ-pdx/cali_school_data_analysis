from pathlib import Path
import re
import csv

data_folder = Path("../CaliSchoolData/data/SuspensionData/rawTextData/")

file_to_open = data_folder / 'susp1112.txt'
file = open(file_to_open, 'rt')
textData = file.read()
file.close()

data_list = textData.splitlines(keepends=True)
data_list = [','.join(line.split(sep='\t')) for line in data_list]

# write to a test csv file
with open('../CaliSchoolData/data/SuspensionData/rawCSVData/testCSV.csv', 'w') as file:
    for line in data_list:
        file.write("%s\n" % line)


with open('../CaliSchoolData/data/SuspensionData/rawCSVData/testCSV.csv') as dirty_csv:
    dirty_csv_reader = csv.reader(dirty_csv)
    with open('clean_csv.csv', 'w', newline='') as clean_csv_file:
        clean_csv_writer = csv.writer(clean_csv_file)

        
        for row in dirty_csv_reader:
            clean_row = []
            for item in row:
                    if item != '':
                        clean_row.append(item)
            clean_csv_writer.writerow(clean_row)
        
        # clean_csv_list = [[item for item in row if item != ''] for row in dirty_csv_reader]
        


# with open('eggs.csv', 'w', newline='') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
