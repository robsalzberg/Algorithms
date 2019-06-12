#!/usr/bin/python

import argparse


def find_max_profit(prices):
# max profit = the second in line price - the first in line price 270-1050=-780
    max_profit = prices[1] - prices[0]
# iterate through the prices
    for i in range(1, len(prices)):
        for j in range(i+1, len(prices)):   
            difference = prices[j] - prices[i]
# 1540-270=1270, 3800-270=3530, 2-270=-268, 3800-1540=2260, 2-1540=-1538
            if difference > max_profit:        # If the difference is greater than the max profit
                max_profit = difference        # set the max profit as the difference 
    return max_profit                          # 1270, 3530 Max Profit $3530


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
