#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  choices = ['rock', 'paper', 'scissors']
  possible_plays = []

  def find_possible_play(n, result=[]):
# Base case
    if n == 0:
      possible_plays.append(result)
      return
    for choice in choices:
# Helper function
# Move towards the base case
      find_possible_play(n-1, result + [choice])
# Call helper function
  find_possible_play(n, [])
  return possible_plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_choices = int(sys.argv[1])
        print(rock_paper_scissors(num_choices))
    else:
        print('Usage: rps.py [num_choices]')
