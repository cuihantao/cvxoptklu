import unittest

class TestBasic(unittest.TestCase):

    def assertEqualLists(self,L1,L2):
        self.assertEqual(len(L1),len(L2))
        for u,v in zip(L1,L2): self.assertEqual(u,v)

    def assertAlmostEqualLists(self,L1,L2,places=7):
        self.assertEqual(len(L1),len(L2))
        for u,v in zip(L1,L2): self.assertAlmostEqual(u,v,places)

    def test_cvxopt_init(self):
        import cvxopt
        cvxopt.copyright()
        cvxopt.license()

    def test_basic(self):
        import cvxopt
        a = cvxopt.matrix([1.0,2.0,3.0])
        b = cvxopt.matrix([3.0,-2.0,-1.0])
        c = cvxopt.spmatrix([1.0,-2.0,3.0],[0,2,4],[1,2,4],(6,5))
        d = cvxopt.spmatrix([1.0,2.0,5.0],[0,1,2],[0,0,0],(3,1))
        self.assertEqualLists(list(cvxopt.mul(a,b)),[3.0,-4.0,-3.0])
        self.assertAlmostEqualLists(list(cvxopt.div(a,b)),[1.0/3.0,-1.0,-3.0])
        self.assertAlmostEqual(cvxopt.div([1.0,2.0,0.25]),2.0)
        self.assertEqualLists(list(cvxopt.min(a,b)),[1.0,-2.0,-1.0])
        self.assertEqualLists(list(cvxopt.max(a,b)),[3.0,2.0,3.0])
        self.assertEqual(cvxopt.max([1.0,2.0]),2.0)
        self.assertEqual(cvxopt.max(a),3.0)
        self.assertEqual(cvxopt.max(c),3.0)
        self.assertEqual(cvxopt.max(d),5.0)
        self.assertEqual(cvxopt.min([1.0,2.0]),1.0)
        self.assertEqual(cvxopt.min(a),1.0)
        self.assertEqual(cvxopt.min(c),-2.0)
        self.assertEqual(cvxopt.min(d),1.0)

    def test_basic_no_gsl(self):
        import sys
        sys.modules['gsl'] = None
        import cvxopt
        cvxopt.normal(4,8)
        cvxopt.uniform(4,8)


    def test_print(self):
        from cvxopt import printing, matrix, spmatrix
        printing.options['height']=2
        A = spmatrix(1.0,range(3),range(3), tc='d')
        print(printing.matrix_repr_default(matrix(A)))
        print(printing.matrix_str_default(matrix(A)))
        print(printing.spmatrix_repr_default(A))
        print(printing.spmatrix_str_default(A))
        print(printing.spmatrix_str_triplet(A))

        A = spmatrix(1.0,range(3),range(3), tc='z')
        print(printing.matrix_repr_default(matrix(A)))
        print(printing.matrix_str_default(matrix(A)))
        print(printing.spmatrix_repr_default(A))
        print(printing.spmatrix_str_default(A))
        print(printing.spmatrix_str_triplet(A))

        A = spmatrix([],[],[],(3,3))
        print(printing.spmatrix_repr_default(A))
        print(printing.spmatrix_str_default(A))
        print(printing.spmatrix_str_triplet(A))

if __name__ == '__main__':
    unittest.main()
