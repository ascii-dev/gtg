def insertion_sort(A):  # O(n^2)
    """
    Sort list of comparable elements into non-decreasing order
    """
    for k in range(1, len(A)):  # from 1 to n-1
        current = A[k]  # current element to be inserted
        j = k  # find correct index j for current
        while j > 0 and A[j-1] > current:  # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = current
