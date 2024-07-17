# Gregor Remec - July 2024

"""
    Algo project goals: 
    - make the algo just off of a description
    - optimize as much as possible before checking solution
    - make a guess at time and space complexity
"""

"""
    Time: O(n^2)
    Space: O(1) for temp variables
"""

def selection_sort(L):
    """Do selection sort on L and return sorted list."""

    mIndex = 0

    for i in range(len(L) - 1):
        mIndex = i
        
        for j in range(i + 1, len(L)):
            if L[j] < L[mIndex]:
                mIndex = j

        if not i == mIndex: # avoid unnecessary swaps
            L[i], L[mIndex] = L[mIndex], L[i] # non-explicit temp variables
    
    return L

'''
    Optimizations / things that I didn't get on my own:
    - you dont need to be explicit with temp variables in python
    - no need for a min value just hold the index
'''

if __name__ == "__main__":
    L = [8, 6, 4, 1, 2, 9, 1]
    print(L)
    print(selection_sort(L))