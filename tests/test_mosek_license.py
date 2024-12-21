import os
import urllib.request
from datetime import datetime
from unittest.mock import patch

import pytest

from mosek_license.license import _url, current, upsert


def test_current():
    try:
        del os.environ["MOSEKLM_LICENSE_FILE"]
    except KeyError:
        # Variable doesn't exist, so nothing to delete
        pass

    with pytest.raises(KeyError):
        current()


def test_mock(resource_dir):
    # https://stackoverflow.com/questions/32043035/python-3-urlopen-context-manager-mocking
    data = open(resource_dir / "license", "rb")

    with patch.object(urllib.request, "urlopen", return_value=data):
        # give some date to the url function to modify today's date
        license = _url(today=datetime.strptime("01-Jan-2025", "%d-%b-%Y").date())

        # read the file again
        with open(resource_dir / "license", newline=None) as f:
            assert license == f.read()


@pytest.mark.parametrize("file", ["license_p1", "license_p2", "license_p3"])
def test_wrong_license(resource_dir, file):
    data = open(resource_dir / file, "rb")

    with pytest.raises(AssertionError):
        with patch.object(urllib.request, "urlopen", return_value=data):
            _url()


def test_expired_license(resource_dir):
    data = open(resource_dir / "license", "rb")

    with pytest.raises(AssertionError):
        with patch.object(urllib.request, "urlopen", return_value=data):
            # give some date to the url function to modify today's date
            _url(today=datetime.strptime("01-Jan-2026", "%d-%b-%Y").date())


def test_upsert(resource_dir):
    # https://stackoverflow.com/questions/32043035/python-3-urlopen-context-manager-mocking
    data = open(resource_dir / "license", "rb")

    with patch.object(urllib.request, "urlopen", return_value=data):
        upsert(today=datetime.strptime("01-Jan-2025", "%d-%b-%Y").date())

        with open(resource_dir / "license", newline=None) as f:
            assert current() == f.read()
