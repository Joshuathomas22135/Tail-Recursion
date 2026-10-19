""" A Python program that uses tail recursion with an accumulator, adds each value as n counts down, and shows how the final result 
is built through repeated recursive calls."""

def tailM(n, acc=1):
    if n <= 1:
        return acc
    return tailM(n-1, n*acc)

print(tailM(12))