from polynomials import *
from tools import *
from functools import reduce
from itertools import product
from collections import Counter

def check_reducible_aux(p, n):
    d = len(p) - 1
    for i, j in sum_eq(d):
        for r, s in product(polys(i, n, monic = True), polys(j, n, monic = True)):
            if polyCompare((polyMod(polyMul(r, s), n)), p):
                return (check_reducible(r, n), check_reducible(s, n))
    return p

def check_reducible(p, n):
    """
    Check if a polynomial p is reducible in the finite field of n elements.
    We assume the polynomial p is in canonical form.
    """
    return flatten(check_reducible_aux(p, n))

def reducible_polys(d, n, monic = False):
    """
    Reutrn the set of reducible polynomials of degree d in the finite field of 
    n elements. Note that the outputed polynomials are tuples.
    """
    return { tuple(polyMod(polyMul(p, q), n)) for i, j in sum_eq(d) 
             for p, q in product(polys(i, n), polys(j, n)) }

def irreducible_polys(d, n, monic = False):
    """
    Returns the set of irreducible polynomials of degree d in the finite field 
    of n elements. Note that the outputed polynomials are tuples.
    """
    if monic:
        return set(filter(lambda x: x[-1] == 1, 
                          polys(d, n).difference(reducible_polys(d, n))))
    else:
        return polys(d, n).difference(reducible_polys(d, n))

if __name__ == "__main__":
    # Test

    # list of factors
    l = [(1, 1), (3, 2, 1), (4, 1, 0, 1), (0, 1), (2, 1)]
    p = polyMod(tuple(reduce(lambda p, q: polyMul(p, q), l)), 5)
    factors = check_reducible(p, 5)
    print(factors)
    assert Counter(factors) == Counter(l)