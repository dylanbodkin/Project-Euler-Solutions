# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:13:26 2022

@author: Dylan Bodkin

Project Euler: Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main(n1=3,n2=5,upper_limit=1000):

    a = [(i+1)*n1      for i in range(int(((upper_limit-1)-(upper_limit-1)%n1)/n1))]
    b = [(i+1)*n2      for i in range(int(((upper_limit-1)-(upper_limit-1)%n2)/n2))]
    c = [(i+1)*(n1*n2) for i in range(int(((upper_limit-1)-(upper_limit-1)%(n1*n2))/(n1*n2)))]
    sum_of_multiples = sum(a)+sum(b)-sum(c)
    
    print(f'The sum of all the multiples of {n1} or {n2} below {upper_limit} is {sum_of_multiples}.')
    return sum_of_multiples

if __name__ == "__main__":
    
    main()
