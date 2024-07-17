# Gregor Remec - July 2024

"""
    Algo project goals: 
    - make the algo just off of a description
    - optimize as much as possible before checking solution
    - make a guess at time and space complexity
"""

"""
    Time: O(n^2)
    Space: O(1) - only temp vars to swap
"""

def swap_insertion_sort(L):
    """Do direct swapping insertion sort on L and return sorted list."""

    for i in range(1, len(L)):

        for j in range(i):

            if L[j] > L[i]:
                L[i], L[j] = L[j], L[i]

    return L

def shuffle_insertion_sort(L):
    """Do shuffling insertion sort on L and return sorted list."""

    for i in range(1, len(L)):
        j = i
        
        while j > 0:
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
            else:
                break
            j -= 1

    return L

def insertion_sort(L):
    return shuffle_insertion_sort(L)

'''
    Optimizations / things that I didn't get on my own:
    - I made swap insertion sort, but shuffle is the true algo
'''

if __name__ == "__main__":
    L = [23, 1, 10, 5, 2]
    print(L)
    print(shuffle_insertion_sort(L))