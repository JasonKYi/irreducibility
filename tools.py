def sum_eq(n):
    """
    Returns the list of tuples (a, b) such that a + b = n. Discards repeated 
    tuples including reordering.
    """
    l = range(int(n / 2) + 1)
    return [(list(map(lambda x: n - x, l))[i], l[i]) for i in l][1:]

def flatten_aux(T):
    if all(not isinstance(t, tuple) for t in T): return (T,)
    elif len(T) == 0: return ()
    else: return flatten(T[0]) + flatten(T[1:])

def flatten(T):
    """ 
    Flatten a nested tuple T into a tuple of tuples.
    """
    return tuple(filter(lambda x: x, flatten_aux(T)))
