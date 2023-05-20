"""
Mosek license
"""

import os
from urllib.request import urlopen

ENV_VARNAME = "MOSEKLM_LICENSE_FILE"


def upsert(server=None):
    """Insert or update an environment varible MOSEKLM_LICENSE_FILE"""
    os.environ[ENV_VARNAME] = _url(server=server)


def current():
    """Get the current license"""
    return os.environ.get(ENV_VARNAME)


def _url(server=None):
    server = server or "http://localhost:8080/mosek"
    with urlopen(server) as page:
        return page.read().decode("utf-8")
