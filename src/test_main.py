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
    def test_sin(self):
        x = Elems.sin(FADiff.new_scal(3))
        assert x.val == pytest.approx(0.1411200080598672)
        assert x.der == pytest.approx(-0.9899924966004454)

        y = 2
        assert Elems.sin(y) == np.sin(y)

    def test_tan(self):
        x = Elems.tan(FADiff.new_scal(3))
        assert x.val == pytest.approx(-0.1425465430742778)
        assert x.der == pytest.approx(-1.020319516942427)
        
        y = 2
        assert Elems.tan(y) == np.tan(y)

    def test_arcsin(self):
        x = Elems.arcsin(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(0.30469265)
        with pytest.warns(RuntimeWarning):
            Elems.arcsin(-19)
        
        y = -0.4
        assert Elems.arcsin(y) == np.arcsin(y)

    def test_arccos(self):
        x = Elems.arccos(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(1.2661036727794992)
        with pytest.warns(RuntimeWarning):
            Elems.arccos(19)
        
        y = -0.4
        assert Elems.arccos(y) == np.arccos(y)

    def test_arctan(self):
        x = Elems.arctan(FADiff.new_scal(0.5))
        assert x.val == pytest.approx(0.4636476090008061)

        y = -0.4
        assert Elems.arctan(y) == np.arctan(y)

    def test_sinh(self):
        x = Elems.sinh(FADiff.new_scal(0.4))
        assert x.val == pytest.approx(0.4107523258028155)

        y = -0.4
        assert Elems.sinh(y) == np.sinh(y)
    
    def test_cosh(self):
        x = Elems.cosh(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(1.04533851)
        assert x.der == pytest.approx(0.30452029)

        y = 4
        assert Elems.cosh(y) == np.cosh(y)

    def test_tanh(self):
        x = Elems.tanh(FADiff.new_scal(1))
        assert x.val == pytest.approx(0.7615941559557649)

        y = 2
        assert Elems.tanh(y) == np.tanh(y)

    def test_log(self):
        x = Elems.log(FADiff.new_scal(0.3))
        assert x.val == pytest.approx(-1.2039728)

        y = 2
        assert Elems.log(y) == pytest.approx(np.log(y) / np.log(np.e))

    # def test_logistic(self):
    #     x = Elems.logistic(FADiff.new_scal(0.3))
    #     assert x.val == np.log(x._val) / np.log(np.e)