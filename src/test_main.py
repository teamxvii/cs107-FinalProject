import pytest
import coverage
from FADiff import FADiff
import Elems
import numpy as np


class TestClass:
    def test_test(self):
        x = 3
        assert x == 3

    def test_neg(self):
        x = FADiff.new_scal(3)
        assert -x.val == -3
        assert -x.der == -1

    def test_add(self):
        x = FADiff.new_scal(3) + 5
        assert x.val == 8
        assert x.der == 1

        y = FADiff.new_scal(3) + FADiff.new_scal(5)
        assert y.val == 8

    def test_radd(self):
        x = 5 + FADiff.new_scal(3)
        assert x.val == 8
        assert x.der == 1

    def test_sub(self):
        x = FADiff.new_scal(3) - 5
        assert x.val == -2
        assert x.der == 1

        y = FADiff.new_scal(3) - FADiff.new_scal(2)
        assert y.val == 1
        assert x.der == 1

    def test_rsub(self):
        x = 3 - FADiff.new_scal(3)
        assert x.val == 0
        assert x.der[0] == 2

    def test_mul(self):
        x = FADiff.new_scal(3) * 3
        assert x.val == 9
        assert x.der == 3

        y = FADiff.new_scal(3) * FADiff.new_scal(4)
        assert y.val == 12
        # assert y.der == 7

    def test_rmul(self):
        x = 3 * FADiff.new_scal(3)
        assert x.val == 9
        assert x.der == 3

    def test_div(self):
        x = FADiff.new_scal(3) / 3
        assert x.val == 1
        assert x.der == pytest.approx(0.3333333333333333)

        y = FADiff.new_scal(3) / FADiff.new_scal(4)
        assert y.val == pytest.approx(0.75)
        # assert y.der == pytest.approx(0.0625)

    def test_rdiv(self):
        x = 3 / FADiff.new_scal(3)
        assert x.val == 1
        assert x.der == pytest.approx(-0.3333333333333333)

    def test_pow(self):
        x = FADiff.new_scal(3) ** 2
        assert x.val == 9
        assert x.der == 6

        y = FADiff.new_scal(3) ** FADiff.new_scal(5)
        assert y.val == 243
        assert y.der[0] == 405

    def test_rpow(self):
        x = 2 ** FADiff.new_scal(3)
        assert x.val == 8
        assert x.der == pytest.approx(5.54517744)


# Elems testing


    def test_exp(self):
        x = Elems.exp(FADiff.new_scal(3))
        assert x.val == pytest.approx(20.085536923187668)
        assert x.der == pytest.approx(20.085536923187668)

        y = 10
        assert Elems.exp(y) == np.exp(y)

    def test_cos(self):
        x = Elems.cos(FADiff.new_scal(3))
        assert x.val == pytest.approx(-0.9899924966004454)
        assert x.der == pytest.approx(-0.1411200080598672)

        y = 2
        assert Elems.cos(y) == np.cos(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(3)
        
        a = Elems.cos(z)
        assert a.val == pytest.approx(-0.9899924966004454)

    def test_sin(self):
        x = Elems.sin(FADiff.new_scal(3))
        assert x.val == pytest.approx(0.1411200080598672)
        assert x.der == pytest.approx(-0.9899924966004454)

        y = 2
        assert Elems.sin(y) == np.sin(y)
        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(3)
        
        a = Elems.sin(z)
        assert a.val == pytest.approx(0.1411200080598672)


    def test_tan(self):
        x = Elems.tan(FADiff.new_scal(3))
        assert x.val == pytest.approx(-0.1425465430742778)
        assert x.der == pytest.approx(1.020319516942427)
        y = 2
        assert Elems.tan(y) == np.tan(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(3)
        a = Elems.tan(z)
        assert a.val == pytest.approx(-0.1425465430742778)

    def test_arcsin(self):
        x = Elems.arcsin(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(0.30469265)
        with pytest.warns(RuntimeWarning):
            Elems.arcsin(-19)

        y = -0.4
        assert Elems.arcsin(y) == np.arcsin(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(0.3)
        a = Elems.arcsin(z)
        assert a.val == pytest.approx(0.30469265)

    def test_arccos(self):
        x = Elems.arccos(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(1.2661036727794992)
        with pytest.warns(RuntimeWarning):
            Elems.arccos(19)

        y = -0.4
        assert Elems.arccos(y) == np.arccos(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(0.3)
        a = Elems.arccos(z)
        assert a.val == pytest.approx(1.2661036727794992)

    def test_arctan(self):
        x = Elems.arctan(FADiff.new_scal(0.5))
        assert x.val == pytest.approx(0.4636476090008061)

        y = -0.4
        assert Elems.arctan(y) == np.arctan(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(0.5)
        a = Elems.arctan(z)
        assert a.val == pytest.approx(0.4636476090008061)

    def test_sinh(self):
        x = Elems.sinh(FADiff.new_scal(0.4))
        assert x.val == pytest.approx(0.4107523258028155)

        y = -0.4
        assert Elems.sinh(y) == np.sinh(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(0.4)
        a = Elems.sinh(z)
        assert a.val == pytest.approx(0.4107523258028155)

    def test_cosh(self):
        x = Elems.cosh(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(1.04533851)
        assert x.der == pytest.approx(0.30452029)

        y = 4
        assert Elems.cosh(y) == np.cosh(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(0.3)
        a = Elems.cosh(z)
        assert a.val == pytest.approx(1.04533851)

    def test_tanh(self):
        x = Elems.tanh(FADiff.new_scal(1))
        assert x.val == pytest.approx(0.7615941559557649)

        y = 2
        assert Elems.tanh(y) == np.tanh(y)

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(1)
        a = Elems.tanh(z)
        assert a.val == pytest.approx(0.7615941559557649)

    def test_log(self):
        x = Elems.log(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(-1.2039728)

        y = 2
        assert Elems.log(y) == pytest.approx(np.log(y) / np.log(np.e))

        z = FADiff()
        z.set_mode('reverse')
        z = z.new_scal(0.3)
        a = Elems.log(z)
        assert a.val == pytest.approx(-1.2039728)

    def test_logistic(self):
        x = FADiff()
        x.set_mode('forward')
        x = x.new_scal(2)
        x = Elems.logistic(x)
        assert x.val == pytest.approx(0.8807970779778823)

    def test_sqrt(self):
        x = Elems.sqrt(FADiff.new_scal(3))
        assert x.val == pytest.approx(1.7320508075688772)

        y = 2
        assert Elems.sqrt(y) == np.sqrt(y)

        z = Elems.sqrt(FADiff.new_scal(-1))
        with pytest.raises(AssertionError):
            assert z.val == 1
    # def return_same_type(self):
    #     x = FADiff.new_vect(np.array([2, 3, 4]))
    #     assert Elems.return_same
    # _type(x)

    # FADiff class
    def test_mode(self):
        x = FADiff()
        x.set_mode('forward')
        assert x._mode == 'forward'
        x.new_scal(3)
        assert x._mode == 'forward'
        x.set_mode('reverse')
        assert x._mode == 'reverse'
        x.new_scal(4)
        x.set_mode('testing')
        assert x._mode != 'forward' or x._mode != 'reverse'

        y = FADiff()
        y.set_mode('forward')
        assert y._mode == 'forward'
        y = y.new_vect(np.array([2,3,4]))
        assert y.der is not None

        z = FADiff()
        z.set_mode('reverse')
        
        z = z.new_vect(np.array([1,2,3]))
        assert FADiff._mode == 'reverse'


        

    # FuncVect class
    # def test_funcvect(self):

        # x = FADiff()
        # x.new_vect(np.array([2,3,4]))
        # assert len(x.val) == 1
        # assert len(x.val[0]) == 3
        # assert type(x.val[0]) is np.ndarray
        # assert type(x) is not np.ndarray
        
    