from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    whole_set = []
    for elem in lst:
        if type(elem) == type([]):
            whole_set += flatten(elem)
        else:
            whole_set += [elem]
    return whole_set


# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    whole_list = []
    if len(lst1) == 0 or len(lst2) == 0:
        whole_list = lst1 + lst2
    elif lst1[0] < lst2[0]:
        whole_list += [lst1[0]] + merge(lst1[1:], lst2)
    else:
        whole_list += merge(lst2, lst1)
    return whole_list
