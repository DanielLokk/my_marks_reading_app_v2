from Exercise import Exercise
from Set import Set
from Day import Day
import re
import pandas as pd
import csv

def readFile():
    # open notes.txt file
    with open("res/notes.txt", "r") as f:
        days = []
        skip_first = False
        list_ex = []
        line = f.readline().rstrip('\n')
        while 1:
            if 'new' in line:
                print('\033[94m' + "New day!" + "\033[0m")
                if skip_first is True:
                    day = Day(line, list_ex)
                    days.append(day)
                skip_first = True
                line = f.readline().rstrip('\n')
            # ex name
            if ':' in line:
                reps = 0
                ex_time = line.split(":")
                ex = Exercise(ex_time[0], ex_time[1])
                while 1:
                    line = f.readline().rstrip('\n')
                    # Set
                    if ('[' in line) & (']' in line):
                        reps = reps + 1
                        set_info = re.split('x |- ', line)
                        slice_object = slice(4, -1)
                        # Set has no weight
                        if len(set_info) == 2:
                            sets = Set(int(set_info[0][slice_object]), int(set_info[1]))
                        else:
                            sets = Set(int(set_info[0][slice_object]), int(set_info[2]), int(set_info[1]))
                        ex.addSet(sets)
                    # save exercise
                    else:
                        ex.setNReps(reps)
                        list_ex.append(ex)
                        break
            if line == '':
                break
    f.close()
    return days

days = readFile()

print(len(days))

# def printFile():
#     for ex in list_exercises:
#         print(ex.whatExercise())
#         print("These are the Sets ->")
#         print(ex.whatSets(), end=" ")
#         print("----------------")

# printFile()

def writeCsv(list_exercises):
    with open("marks.csv", 'w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        wr.writerow(['Name', 'Rest_time', 'n_reps'])
        for ex in list_exercises:
            wr.writerow([ex.name, ex.rest_time, ex.n_reps])

writeCsv(days[0].routine)

import os 
import glob
import csv
from xlsxwriter.workbook import Workbook

for csvfile in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()

