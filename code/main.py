from pathlib import Path
import re
import csv
import pandas as pd
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

TEMP_PATH = '../CaliSchoolData/temp/'
def main():
    
    # Use a tkinter askopenfilename gui to select the filepath
    # TODO: create check on file type to make sure a txt file is being selected
    
    Tk().withdraw()
    file_path = askopenfilename()
    convertTextToCSV(file_path)
            
def convertTextToCSV(file_path):

    # Open the text file using the file_path parameter
    opened_file = open(file_path, 'rt')
    raw_text_data = opened_file.read()
    opened_file.close()

    # Move each line of the text file into a list, then replace each tab with a comma
    data_list = raw_text_data.splitlines(keepends=True)
    data_list = [','.join(line.split(sep='\t')) for line in data_list]

    with open(TEMP_PATH + 'tempCSV.csv', 'w') as temp_csv:
        for line in data_list:
            temp_csv.write("%s\n" % line)

    with open(TEMP_PATH + 'tempCSV.csv') as temp_csv:
        temp_csv_reader = csv.reader(temp_csv)
        with open('clean_csv.csv', 'w', newline='') as clean_csv_file:
            clean_csv_writer = csv.writer(clean_csv_file)
            
            for row in temp_csv_reader:
                clean_row = []
                for item in row:
                        if item != '':
                            clean_row.append(item)
                clean_csv_writer.writerow(clean_row)
    
    os.remove(TEMP_PATH + 'tempCSV.csv')

main()
        

