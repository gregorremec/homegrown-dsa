# Gregor Remec - July 2024

"""
    Algo project goals: 
    - make the algo just off of a description
    - optimize as much as possible before checking solution
    - make a guess at time and space complexity
"""

"""
    Time: 
    Space: 
"""

import random

def quick_sort(L):
    """Do quick sort on L and return sorted list."""

    if len(L) <= 1:
        return L
    
    tpi = 0 # true pivot index
    spi = len(L) - 1 # starting pivot index

    for i in range(len(L) - 1):
        if L[i] <= L[spi]:
            L[i], L[tpi] = L[tpi], L[i] # swap values under the pivot to behind it
            tpi += 1

    L[spi], L[tpi] = L[tpi], L[spi] # swap the pivot to it's correct position at the end

    
    return quick_sort(L[:tpi]) + [L[tpi]] + quick_sort(L[(tpi+1):]) # python lists maybe not efficient

'''
    Optimizations / things that I didn't get on my own:
    - TODO random pivot so sorted lists don't ruin performance
    - TODO I used splicing instead of in place sort
    - i thought it was stable... maybe not
    - TODO revist this one
'''

if __name__ == "__main__":
    L = [8, 4, 2, 4, 5]
    print(L)
    print(quick_sort(L))
