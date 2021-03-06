from os import chdir
from glob import glob
import pandas as pdlib

def produceOneCSV(list_of_files, file_output):
    result_obj = pdlib.concat([pdlib.read_csv(file) for file in list_of_files])
    result_obj.to_csv(file_out, index = False, encoding="utf-8")

csv_file_path = '/content/csv'
chdir(csv_file_path)

file_pattern = ".csv"
list_of_files = [file for file in glob('*.{}'.format(file_pattern))]
print(list_of_files)

file_out = "ConsolidateOutput.csv"
produceOneCSV(list_of_files, file_out)