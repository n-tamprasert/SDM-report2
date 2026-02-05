#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^[1-9][0-9]*$') # Correction:regex to match a positive number (integer only)
        if p.match(ai) and p.match(bi): # Correction:check if A and B are both match the regex
                a=float(ai)
                b=float(bi)
                if 0<a<1000 and 0<b<1000: # Correction:fixed the conditions for valid inputs
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
