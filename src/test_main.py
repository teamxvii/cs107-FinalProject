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

    def test_cos(self):
        x = Elems.cos(FADiff.new_scal(3))
        assert x.val == pytest.approx(-0.9899924966004454)
        assert x.der == pytest.approx(-0.1411200080598672)

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
