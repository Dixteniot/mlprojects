# testcode02a.py

import expectation as xp
import pprint

def main():
    print('0: %s'%(xp.decimalToBinary(0)))
    print('1: %s'%(xp.decimalToBinary(1)))
    print('2: %s'%(xp.decimalToBinary(2)))
    print('3: %s'%(xp.decimalToBinary(3)))
    print('7: %s'%(xp.decimalToBinary(7)))
    print('8: %s'%(xp.decimalToBinary(8)))
    print('15: %s'%(xp.decimalToBinary(15)))
    print('16: %s'%(xp.decimalToBinary(16)))
    print('31: %s'%(xp.decimalToBinary(31)))
    print('32: %s'%(xp.decimalToBinary(32)))
    print('63: %s'%(xp.decimalToBinary(63)))
    print('64: %s'%(xp.decimalToBinary(64)))
    table = xp.truthTable()
    pprint.pprint(table)

if __name__ == '__main__':
    main()
