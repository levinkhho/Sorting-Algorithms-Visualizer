def slowSort(array, left, right):
    """
    Slow Sort is a divide and conquer algorithm like Merge Sort.
    Like Merge Sort, it starts by dividing the input list in half and
    recursively sorting each half. Unlike Merge Sort, which then merges
    the two halves in an efficient way, Slow Sort does so in a very
    inefficient way: it selects the maximum of the two largest elements
    from each half, places it at the end of the list, and then recursively
    calls itself on the remaining list.

    The creators of Slow Sort, Andrei Broder and Jorge Stolfi, classified
    it not as a divide and conquer algorithm, but as a "multiply and
    surrender" algorithm.
    
    Unlike Bogo Sort, Slow Sort is "non-decreasing", in that every step
    technically gets you closer to a sorted list (or, more often, does
    nothing).

    Time complexity: not yet proven. A lower bound on Slow Sort is
    \Omega(n^{\log_2(n)/(2+\epsilon)}) for any \epsilon>0, according to
    Broder and Stolfi in their book Pessimal Algorithms and Simplexity
    Analysis.
    """
    if left >= right:
        return

    # Display current search field
    yield array, -1, -1, left, right

    mid = (left + right) // 2
    yield from slowSort(array, left, mid)  # Recursively sort the first half
    yield from slowSort(array, mid + 1, right)  # Recursively sort the second half

    # Display comparison of largest of two halves
    yield array, mid, right, left, -1

    # If the max. of the first half is greater than the max. of the second, swap them
    if array[right] < array[mid]:
        temp = array[right]
        array[right] = array[mid]
        array[mid] = temp
        # Display swap
        yield array, right, mid, left, -1

    # Recursively call slowSort on the current array minus the last (largest) element.
    yield from slowSort(array, left, right-1)
