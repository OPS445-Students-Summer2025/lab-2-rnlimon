#!/usr/bin/env python3

# Using arguments
import sys

scriptname = sys.argv[0]

# Using if statement with arguments and print usage message
if len(sys.argv) != 3:
    print('Usage: ' + scriptname + ' name age')
    sys.exit()

# Enter info for name and age as an arguments
name = sys.argv[1]
age = sys.argv[2]

# Print the output based on the name and age arguments
print('Hi ' + name + ', you are ' + str(age) + ' years old.')

