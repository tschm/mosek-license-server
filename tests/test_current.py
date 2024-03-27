import pytest

from mosek_license.license import current


def test_current():
    with pytest.raises(KeyError):
        current()
