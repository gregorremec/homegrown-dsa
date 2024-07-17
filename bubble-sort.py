# Gregor Remec - July 2024

"""
    Algo project goals: 
    - make the algo just off of a description
    - optimize as much as possible before checking solution
    - make a guess at time and space complexity
"""

"""
    Time: O(n^2)
    Space: O(1) just temp variables
"""

def bubble_sort(L):
    """Do bubble sort on L and return sorted list."""

    
    for i in range(len(L)):
        swapOccured = False

        # - i so that you don't redo already sorted values
        for j in range(len(L) - i - 1):

            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1],  L[j]
                swapOccured = True

        # if there are no swaps made in a full pass then the list is sorted
        if swapOccured is False:
            break

    return L
    
'''
    Optimizations / things that I didn't get on my own:
    - not going through the already sorted values at the end of the list
    - the swapOccured boolean to check if the list is sorted early
'''

if __name__ == "__main__":
    L = [8, 6, 9, 1, 3, 2 , 5, 6, 2, 5, 1, 1]
    print(L)
    print(bubble_sort(L))