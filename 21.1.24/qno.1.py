Given an integer, , perform the following conditional actions

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird

Sample Input 0

3
Sample Output 0

Weird

---------------------x------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input().strip())

if __name__ == '__main__':
    if n%2!=0:
        print("Weird")
    else:
        if n in range(2,5):
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        elif n>21:
            print("Not Weird")
