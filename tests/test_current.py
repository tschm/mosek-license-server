import os
from unittest.mock import MagicMock, patch

import pytest

from mosek_license.license import current, upsert


def test_current():
    with pytest.raises(KeyError):
        current()


@patch("urllib.request.urlopen")
def test_cm(mock_urlopen):
    # https://stackoverflow.com/questions/32043035/python-3-urlopen-context-manager- mocking

    cm = MagicMock()
    cm.read.return_value = b"maffay"
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm

    upsert(server="http://localhost:8080/mosek")
    assert os.environ["MOSEKLM_LICENSE_FILE"] == "maffay"
