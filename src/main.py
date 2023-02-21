import os

inputFileDir = '../data/input.csv'

# error check file path
if not os.path.exists(inputFileDir):
    print('Cannot find ' + inputFileDir + '.')
    quit()

# open input file
inputFile = open(inputFileDir, 'r')

