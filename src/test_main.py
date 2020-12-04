import pytest
from FADiff import FADiff

class TestClass:
    def test_neg(self):
        x = -FADiff(3, 1)
        assert x.val == -3
        assert x.der == -1

    def test_add(self):
        x = FADiff(3, 1) + 5
        assert x.val == 8
        assert x.der == 1

        y = FADiff(3, 0) + FADiff(5, 0)
        assert y.val == 8
        assert y.der == 0

    def test_radd(self):
        x = 5 + FADiff(3, 1)
        assert x.val == 8
        assert x.der == 1

    def test_sub(self):
        x = FADiff(3, 1) - 5
        assert x.val == -2
        assert x.der == 1

        y = FADiff(3, 1) - FADiff(2, 1)
        assert y.val == 1
        assert x.der == 1

    def test_rsub(self):
        x = 3 - FADiff(3, 1)
        assert x.val == 0
        assert x.der == 1

    def test_mul(self):
        x = FADiff(3, 1) * 3
        assert x.val == 9
        assert x.der == 3
        y = FADiff(3, 1) * FADiff(4, 1)
        assert y.val == 12
        assert y.der == 7

    def test_rmul(self):
        x = 3 * FADiff(3, 1)
        assert x.val == 9
        assert x.der == 3

    def test_div(self):
        x = FADiff(3, 1) / 3
        assert x.val == 1
        assert x.der == pytest.approx(0.3333333333333333)

        y = FADiff(3, 1) / FADiff(4, 1)
        assert y.val == pytest.approx(0.75)
        assert y.der == pytest.approx(0.0625)

    def test_rdiv(self):
        x = 3 / FADiff(3, 1)
        assert x.val == 1
        assert x.der == pytest.approx(-0.3333333333333333)

    def test_pow(self):
        x = FADiff(3, 1) ** 2
        assert x.val == 9
        assert x.der == 6

        y = FADiff(3, 1) ** FADiff(5, 1)
        assert y.val == 243
        assert y.der == 405

    def test_rpow(self):
        x = 2 ** FADiff(3, 1)
        assert x.val == 8
        assert x.der == pytest.approx(5.54517744)

    def test_exp(self):
        x = FADiff.exp(FADiff(3, 1))
        assert x.val == pytest.approx(20.085536923187668)
        assert x.der == pytest.approx(20.085536923187668)

    def test_cos(self):
        x = FADiff.cos(FADiff(3, 1))
        assert x.val == pytest.approx(-0.9899924966004454)
        assert x.der == pytest.approx(-0.1411200080598672)

    def test_sin(self):
        x = FADiff.sin(FADiff(3, 1))
        assert x.val == pytest.approx(0.1411200080598672)
        assert x.der == pytest.approx(-0.9899924966004454)

    def test_tan(self):
        x = FADiff.tan(FADiff(3, 1))
        assert x.val == pytest.approx(-0.1425465430742778)
        assert x.der == pytest.approx(1.020319516942427)
