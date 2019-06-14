#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
# Base code
  if(n==1 or n==0):
        return 1
  elif(n==2):
        return 2
  else:
# If you eat 1 cookies then there are n-1 cookies remaining
# If you eat 2 cookies then there are n-2 cookies remaining
# If you eat 3 cookies then there are n-3 cookies remaining
# Repeat until there are no cookies left n=0
        return (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
