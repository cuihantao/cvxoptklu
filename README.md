CVXOPTKLU
======

KLU Add-On for CVXOPT, Python Software for Convex Optimization 

This repository is a fork of the CVXOPT with KLU fork by Uriel Sandoval (@sanurielf).

* [CVXOPT Website](http://cvxopt.org)
* [CVXOPT with KLU](https://github.com/sanurielf/cvxopt)

## FAQ
Q: "A must be square sparse matrix" error when calling `klu.linsolve`
A: This happens when you passed a scipy.sparse matrix to `klu.linsolve`, which only takes `cvxopt.spmatrix`. 
Use the following wrapper:

```
def klu_linsolve(A, b):
    """
    KLU wrapper function for linear system solve A x = b (author: @SanPen)
    :param A: System matrix
    :param b: right hand side
    :return: solution
    """
    A2 = A.tocoo()
    A_cvxopt = cvxopt.spmatrix(A2.data, A2.row, A2.col, A2.shape, 'd')
    x = cvxopt.matrix(b)
    klu.linsolve(A_cvxopt, x)
    return np.array(x)[:, 0]
```
