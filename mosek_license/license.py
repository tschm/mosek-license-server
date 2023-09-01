# Copyright 2023 Thomas Schmelzer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Mosek license
"""
from __future__ import annotations

import os
from urllib.request import urlopen

ENV_VARNAME = "MOSEKLM_LICENSE_FILE"


def upsert(server=None):
    """Insert or update an environment varible MOSEKLM_LICENSE_FILE"""
    os.environ[ENV_VARNAME] = _url(server=server)


def current():
    """Get the current license"""
    try:
        return os.environ[ENV_VARNAME]
    except KeyError:
        raise KeyError(
            "The environment variable MOSEKLM_LICENSE_FILE is not set. "
            "Please use the upsert function to set it."
        )


def _url(server=None):
    server = server or "http://localhost:8080/mosek"
    with urlopen(server) as page:
        return page.read().decode("utf-8")
