import urllib.request
from datetime import datetime
from unittest.mock import patch

import pytest

from mosek_license.license import _url, current


def test_current():
    with pytest.raises(KeyError):
        current()


def test_mock(resource_dir):
    # https://stackoverflow.com/questions/32043035/python-3-urlopen-context-manager-mocking
    data = open(resource_dir / "license", "rb")

    with patch.object(urllib.request, "urlopen", return_value=data):
        # give some date to the url function to modify today's date
        license = _url(today=datetime.strptime("01-Jan-2025", "%d-%b-%Y").date())

        # read the file again
        with open(resource_dir / "license") as f:
            assert license == f.read()  # .decode("utf-8")
