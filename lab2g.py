#!/usr/bin/env python3

# Author: Raffy Limon
# Author ID: rnlimon
# Date Created: 2025/05/21

import sys

# assign the value of 3 to an object named timer when there is no arguments provided
if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

# WHILE loop that repeats until (and not including when) timer equals 0
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')