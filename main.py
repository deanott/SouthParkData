"""

Parsing compoennts to extract character specific message responses.

Takes dummy approach that all messages said before characater is directed to the character

"""
import csv
import re
import argparse


FILE_PATH = "All-seasons.csv"

main_msg_res = []

def csv_convo_parser(obj, name):
    reader = csv.reader(obj)
    
    main_res = ''
    prev_row = ''

    for row in reader:
        if main_res != '':
            print(prev_row[2], "---", prev_row[3][:-1])
            print(name, ":---", main_res)

            main_msg_res.append( (prev_row[3],main_res) )
            
            main_res = ''
        elif re.match(name, row[2]):
            main_res += row[3][:-1]
        else:
            prev_row = row

    print(main_msg_res)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("character", help="Main name of character to gather all responses from. The name is case insensitive.")
    args = parser.parse_args()
    print(args.character)

    name = '(?i)' + args.character 

    with open(FILE_PATH, "r") as o:
        print("Processing conversations: ", name)
        csv_convo_parser(o, name)