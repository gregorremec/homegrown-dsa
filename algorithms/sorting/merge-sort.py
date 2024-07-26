# Gregor Remec - July 2024

"""
    Algo project goals: 
    - make the algo just off of a description
    - optimize as much as possible before checking solution
    - make a guess at time and space complexity
"""

"""
    Time: O(nlogn) - * for leetcode Q4 learn binary search.
    Space: O(n)
"""

def merge_sort(L):
    """Do merge sort on L and return sorted list."""

    if len(L) <= 1:
        return L
    else:
        split = len(L) // 2
        return _merge(merge_sort(L[:split]), merge_sort(L[split:]))
    
    

def _merge(L1, L2):
    """ Helper function to merge two lists."""

    length = len(L1) + len(L2)
    merged = [0] * length

    L1index = 0
    L2index = 0
    
    for i in range(length):
        
        if L1index == len(L1):
            merged[i] = L2[L2index]
            L2index += 1
        elif L2index == len(L2):
            merged[i] = L1[L1index]
            L1index += 1
        elif L1index < len(L1) and L1[L1index] <= L2[L2index]:
            merged[i] = L1[L1index]
            L1index += 1
        elif L2index < len(L2) and L1[L1index] > L2[L2index]:
            merged[i] = L2[L2index]
            L2index += 1

    return merged

'''
    Optimizations / things that I didn't get on my own:
    - had to read a little more on merge step, but got it eventually
    - better base case handling, and not reassigning L in the main function
'''

if __name__ == "__main__":
    L = [8, 6, 9, 1, 4, 2, 34, 5]

    print(L)
    print(merge_sort(L))
