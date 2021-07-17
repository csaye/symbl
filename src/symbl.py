from parser import parse
from os.path import isfile
import sys

# get system arguments
args = sys.argv

# if no program given
if len(args) < 2:
    # throw error and quit
    print('error: no program given')
    print('usage: ./run.sh <program>')
    sys.exit()

# get program path
path = args[1]

# if no program at path
if not isfile(path):
    # throw error and quit
    print('error: invalid program given')
    print('usage: ./run.sh <program>')
    sys.exit()

# open program file
with open(path) as file:
    # read program and parse
    program = file.read()
    parse(program)
