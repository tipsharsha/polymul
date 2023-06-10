def primitiveRootOfUnity(n, q):
    """Find a primitive n-th root of unity mod q if it exists.

    I.e., w, s.t. w^n = 1 mod q and w^k != 1 mod q for all k < n.
    Parameters
    ----------
    n : int
    q : int
        modulus.
    Returns
    ----------
    int
        n-th root of unity modulo q.
    """
    for i in range(2,q):
        if pow(i, n, q) == 1:
            # i is an n-th root of unity, but it may not be primitive
            # check by making sure i^j != 1 mod q for 1<=j<n
            isPrimitive = True
            for j in range(1,n):
                if pow(i, j, q) == 1:
                    isPrimitive = False
                    break
            if isPrimitive:
                return i

print(primitiveRootOfUnity(5,11))
