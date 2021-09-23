#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    print(len(max(bin(n).strip("0b").split("0"))))
