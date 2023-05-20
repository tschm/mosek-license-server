"""
Mosek license
"""

import os
from urllib.request import urlopen

ENV_VARNAME = "MOSEKLM_LICENSE_FILE"


def upsert():
    """Insert or update an environment varible MOSEKLM_LICENSE_FILE"""
    os.environ[ENV_VARNAME] = _url()


def current():
    """Get the current license"""
    return os.environ.get(ENV_VARNAME)


def _url():
    with urlopen(
        f"https://localhost:8080/licenses/mosek"
    ) as page:
        return page.read().decode("utf-8")
