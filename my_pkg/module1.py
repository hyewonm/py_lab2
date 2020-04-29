#!/usr/bin/python3

def result1():
    binN = input('input binary number : ')
    num = int(binN, 2)
    print('OCT> ', format(num,'o'))
    print('DEX> ', num)
    print('HEX> ', format(num, 'X'))
