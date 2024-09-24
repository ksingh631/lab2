#!/usr/bin/env python3
# Author: Kushagra Singh
# Author ID: ksingh631
# Date Created: 2024/09/24

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
