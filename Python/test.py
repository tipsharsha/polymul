from poly import Poly
import common
import sys
import ntt
a = Poly.random(n, q)
b = Poly.random(n, q)
def testcase_cyclic_ntt(a,b,n, q, printPoly=True):
    """Random test of NTT multiplication for Zq[x]/(x^n-1) (`polymul_cyclic_ntt`).

    Parameters
    ----------
    n : int
    
        number of coefficients of input polynomials.
    q : int
        modulus.
    printPoly : boolean
        flag for printing inputs and outputs.
    Returns
    ----------
    int
        0 if test is successful, 1 otherwise.
    """
    print(f"Testing naive cyclic NTT multiplication (i.e., mod x^n - 1) with q={q}, n={n}")
    
    if printPoly: print("a=", a)
    if printPoly: print("b=", b)

    # compute reference product using schoolbook for comparison
    c_ref = a*b
    # reduce mod x^n - 1
    c_red = Poly(c_ref.coeffs[:n], q)
    for i in range(n, c_ref.n):
        c_red.coeffs[i-n] += c_ref.coeffs[i]
    c_red.reduce()

    if printPoly: print("a*b (ref)=", c_red)
    c = polymul_cyclic_ntt(a, b)
    if printPoly: print("c (cyclic NTT)=", c)
    print(f"equal: {c == c_red}")
    if c == c_red:
        return 0
    else:
        return 1