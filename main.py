"""

Parsing compoennts to extract character
specific messages.

"""
import csv
import re

FILE_PATH = "All-seasons.csv"
MAIN_CHAR = "Stan"

main_msg_res = []

def csv_parser(obj):
    reader = csv.reader(obj)
    
    main_res = ''
    prev_row = ''

    for row in reader:
        if main_res != '':
            print(prev_row[2], "---", prev_row[3][:-1])
            print(MAIN_CHAR, ":---", main_res)

            main_msg_res.append( (prev_row[3],main_res) )
            
            main_res = ''
        elif re.match(row[2], MAIN_CHAR):
            main_res += row[3][:-1]
        else:
            prev_row = row



if __name__ == "__main__":
    with open(FILE_PATH, "r") as o:
        print("Parsing conversations")
        csv_parser(o)