import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open(args.filename, "r") as file:
    # this script contains a bunch of individual regexes for common footnote/non-corpus patterns and deletes lines that contain them
    clean_name = ("_clean.").join(args.filename.split("."))
    print("clean name: ", clean_name)
    output = open(clean_name, "w")
    # starting with number followed by period or colon or comma
    startsWithNumber = re.compile('\d+[\.|\:|\,]')
    onlyNumbers = re.compile('^[0-9 ()]+$')
    startsWithBracket = re.compile('^\[')
    startsWithLetterAndPeriod = re.compile('^\w+\.')
    # alphanumeric regex = re.compile('(^[^\s\w]|_)+')
    # this worked! but realized a ton of the lil poems and stuff start nonAlphanumeric
    #startsNonAlphaNumeric = re.compile('^[^\s\w\'\"]')
    f = file.read()
    newF = ''
    for line in f.splitlines():
        print('line')
        if not startsWithNumber.match(line) and not startsWithBracket.match(line) and not startsWithLetterAndPeriod.match(line) and not onlyNumbers.match(line):
            output.write(line + '\n')
        else:
            #            print('match starts with number: ', startsWithNumber.match(line))
            #            print('match starts with bracket: ',
            #                  startsWithBracket.match(line))
            print('match starts with letter and period: ',
                  startsWithLetterAndPeriod.match(line))
            print(line)
    output.close()
    file.close()
