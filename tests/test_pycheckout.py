
import pytest

from ..pycheckout import PyCheckout, PyCheckoutError


class TestPyCheckout:
    def test_pycheckout_init_no_repo_path(self):
        PyCheckout()
