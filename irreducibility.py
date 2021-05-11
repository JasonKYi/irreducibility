from polynomials import *
from tools import *
from functools import reduce
from itertools import product
from collections import Counter

def check_reducible_aux(p, n, monic):
    d = len(p) - 1
    for i, j in sum_eq(d):
        for r, s in product(polys(i, n, monic = monic), polys(j, n, monic = monic)):
            if polyCompare((polyMod(polyMul(r, s), n)), p):
                return (check_reducible_aux(r, n, monic), check_reducible_aux(s, n, monic))
    return p

def check_reducible(p, n, monic = False):
    """
    Check if a polynomial p is reducible in the finite field of n elements.
    We assume the polynomial p is in canonical form.
    """
    return flatten(check_reducible_aux(p, n, monic))

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
    n = 5
    # l = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
    """ CAN'T DO NEGATIVE COEFFICIENTS! """
    p = (3, 1, 0, 1) # polyMod(tuple(reduce(lambda p, q: polyMul(p, q), l)), n)
    print(polyPrint(p))

    factors = check_reducible(p, n, monic = True)
    print(list(map(polyPrint, factors)))
    # assert Counter(factors) == Counter(map(lambda x: tuple(polyMod(x, n)), l))