#!/bin/python3

import math
import os
import random
import re
import sys


 
#
# Complete the 'maximumContainers' function below.
#
# The function accepts STRING_ARRAY scenarios as parameter.
#

def maximumContainers(scenarios):
  for i in scenarios:
    a,b,c = map(int,i.split())
    X = a//b
    Y = X
    temp = 0
    while Y>1:  
        if Y%c==1:
            Y = Y//c
            temp=temp + Y + 1
        else:
            Y = Y//c
            temp = temp + Y

    ans = X+temp
    print(ans)
    
if __name__ == '__main__':
    scenarios_count = int(input().strip())

    scenarios = []

    for _ in range(scenarios_count):
        scenarios_item = input()
        scenarios.append(scenarios_item)
    
    maximumContainers(scenarios)
