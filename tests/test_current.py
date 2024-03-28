from unittest.mock import MagicMock, patch

import pytest

from mosek_license.license import _url, current


def test_current():
    with pytest.raises(KeyError):
        current()


@patch("urllib.request.urlopen")
def test_server(mock_urlopen):
    # https://stackoverflow.com/questions/32043035/python-3-urlopen-context-manager- mocking

    mock = MagicMock()
    mock.read.return_value = b"maffay"
    mock.__enter__.return_value = mock
    mock_urlopen.return_value = mock

    assert _url(server="http://localhost:8080/mosek") == "maffay"

    # assert os.environ["MOSEKLM_LICENSE_FILE"] == "maffay"
