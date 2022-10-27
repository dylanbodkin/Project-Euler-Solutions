# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26  2022
@author: Dylan Bodkin

Project Euler: Problem 3: 
    Largest prime factor
    
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n):
    for i in range(2, int(n**.5) + 1):
        if (n % i == 0):
            is_prime = False
            return False
    return True

def main(n=600851475143):
    factors = []
    i = 2
    while i <= (n**.5):
        if is_prime(i):
            if n%i==0:
                factors.append(i)
                
                a = n
                for j in factors:
                    a /= j
                if a == 1:
                    break
        i+=1
    answer = max(factors)
    print(f'The largest prime factor of the number {n} is {answer}.')
    return answer

if __name__ == "__main__":
    main()