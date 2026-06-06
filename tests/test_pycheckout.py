import random
import string
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pytest_mock import MockFixture

from pycheckout.pycheckout import PyCheckout, PyCheckoutError


class TestPyCheckout:
    def test_pycheckout_init_no_repo_path(self):
        PyCheckout()

    def test_pycheckout_init_repo_is_invalid(self, mocker: MockFixture):
        mocker.patch("pygit2.discover_repository")
        non_existent_repo = "".join(random.choices(string.ascii_lowercase, k=7))
        with pytest.raises(PyCheckoutError) as err:
            PyCheckout(repo_path=non_existent_repo)
        assert str(err.value) == f'Git repository not found at "{non_existent_repo}"'
