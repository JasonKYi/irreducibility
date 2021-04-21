from itertools import product
from functools import reduce
from copy import copy

# We set up some basic infrastructures for working with polynomials as a list
# e.g. we represent 3x^3 + x - 2 as the list [-2, 1, 0, 3]

def polyEval(p, x):
    """ Evaluates the polynomial p at x. """
    return sum([p[i] * x ** i for i in range(len(p))])

def polyCompare(p, q):
    """ Check if the two polynomials are equal. """
    return all([p[i] == q[i] for i in range(max(len(p), len(q)))])

def polyAddAux(p, q):
    """ Find the coefficients of p + q assuming deg p >= deg q. """
    l = len(q)
    return [p[i] + q[i] for i in range(l)] + p[l:]

def polyAdd(p, q):
    """ Find the coefficients of p + q. """
    if len(p) >= len(q):
        return polyAddAux(p, q)
    else: 
        return polyAddAux(q, p)

def polyMul(p, q):
    """ Find the coefficients of p * q. """

    coefs = [0 for _ in range(len(p) + len(q) - 1)]
    for i, j in product(range(len(p)), range(len(q))):
        coefs[i + j] += p[i] * q[j]

    return coefs

def polySmul(p, a):
    """ Find the coefficients of a * p where a is a scalar. """
    return [a * val for val in p]

def polySub(p, q):
    """ Find the coefficients of p - q. """
    return polyAdd(p, polySmul(q, -1))

def polyMod(p, n):
    """ Return the canonical form of a polynomial in the finite field of n elements. """
    return [val % n for val in p]

def polys(d, n, monic = False):
    """
    Returns the list of all polynomials of degree d in the finite field of n 
    elements. Note that the outputed polynomials are tuples.
    """
    l = [range(n) for _ in range(d)] + [range(1, n)]
    s = set(map(lambda x: tuple(x), product(*l)))
    if monic: return set(filter(lambda x: x[-1] == 1, s))
    else: return s

def polyPrint(p):
    """
    Return the string representing the given polynomial.
    """
    return " + ".join(([str(p[i]) for i in range(1) if p[0] != 0] + 
        [f"{a}x^{i}" for i, a in enumerate(p) if a != 0][1:])[::-1])
