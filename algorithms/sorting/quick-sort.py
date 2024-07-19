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

def quick_sort(L):
    """Do quick sort on L and return sorted list."""

    if len(L) <= 1:
        return L
    
    tpi = 0 # true pivot index
    spi = len(L) - 1 # starting pivot index TODO look into randomness optimization

    for i in range(len(L) - 1):
        if L[i] <= spi:
            L[i], L[tpi] = L[tpi], L[i] # swap values under the pivot to behind it
            tpi += 1

    L[spi], L[tpi] = L[tpi], L[spi] # swap the pivot to it's correct position at the end

    
    return quick_sort(L[:tpi]) + quick_sort(L[tpi:])

'''
    Optimizations / things that I didn't get on my own:
    - 
'''

if __name__ == "__main__":
    L = [8, 6, 9, 1]
    print(L)
    print(quick_sort(L))