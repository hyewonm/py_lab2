#!/usr/bin/python3
if __name__=='__main__':
    import module1
    import module2
    import sys
    import re
    N = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ?"))
    while N != 3:
        if N == 1: 
            module1.result1()
        elif N == 2:
            module2.result2()
        N = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ?"))    
    sys.exit()

