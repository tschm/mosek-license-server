# Mosek License Server

[![Linting](https://github.com/tschm/mosek-license-server/actions/workflows/linting.yml/badge.svg)](https://github.com/tschm/mosek-license-server/actions/workflows/linting.yml)
[![PyPI version](https://badge.fury.io/py/mosek-license-server.svg)](https://badge.fury.io/py/mosek-license-server)
[![Apache 2.0 License](https://img.shields.io/badge/License-APACHEv2-brightgreen.svg)](https://github.com/tschm/mosek-license-server/blob/main/LICENSE)
[![PyPI download month](https://img.shields.io/pypi/dm/mosek-license-server.svg)](https://pypi.python.org/pypi/mosek-license-server/)

Using a [nginx image](https://hub.docker.com/_/nginx/) we expose a Mosek license
on a server to be accessible from various research machines without sharing the actual
license file in the underlying repositories.

This repository serves two purposes. It exposes the server but it is also the home
for a little Python package to inject the license into your programs.

We solve a common problem here. Assume $20$ researchers work on $50$ different strategies.
Using local copies of the same license file is a tedious exercise as
the file needs to get updated once a year.
Rather, each strategy would connect to the server to fetch a license using the mosek_license
Python package. Once the strategy expires we only need to update the server.
No change for the strategies is required.

## License server

### Copy your license file into folder

Copy the license file you have received (from Mosek) into the `web` folder.
Name it `mosek`.

The file should look like

```bash
START_LICENSE
VENDOR MOSEKLM
# PSN-4183
FEATURE PTS MOSEKLM 10 31-jan-2024 uncounted ...
# PSN-4182
FEATURE PTON MOSEKLM 10 31-jan-2024 uncounted ...
END_LICENSE
```

### Start the nginx server

Share the web folder (after you have copied your personal Mosek license into)
via

```bash
docker run --name mosek -v $PWD/web:/usr/share/nginx/html:ro -p 8080:80 -d nginx
```

The license will now be exposed via `http://localhost:8080/mosek`

As an alternative you can run the script

```bash
./start_server.sh
```

## The mosek_license module

Install via

```bash
pip install mosek-license-server
```

and then

```python
import mosek

from mosek_license import license

license.upsert(server="http://localhost:8080/mosek")
```

## Problems

In case you experience problems please check:

- the license file is named `mosek`
- the license file starts with `START_LICENSE`
- the license file ends with `END_LICENSE`
- the dates in the license file are still in the future
- the server is running, e.g. docker ps -all (and check for mosek)
- you can download a license file from the server, e.g. curl <http://localhost:8080/mosek>
- you can run the demo in the demo folder

Still lost? Please open an issue.
