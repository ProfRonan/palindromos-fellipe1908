"""Main functions"""
import re

def is_palindrome(string: str) -> bool:
    h = re.sub(r'[.,"\'-?:!;]', "", string)
    a = h.lower()
    p = a.split()
    j ="".join(p)
    inverter = ""
    for b in range(len(j) -1, -1, -1):
        
        inverter += (j[b])
    if inverter == j:
        print("é um palindromo")
        return True
    else:
        print("n é um palindromo")
        return False
if __name__ == '__main__':
    is_palindrome()