# Mosek License Server

Using the [nginx image](https://hub.docker.com/_/nginx/) we expose a Mosek license
on a server to be accessible from various research machines without sharing the actual
license file in the underlying repos.

## Usage

### Copy your license file into folder 

Copy the license file you have received (from Mosek) into the licenses folder.
Name is ```mosek'''

### Start the nginx server

Share the licenses folder (after you have copied your personal Mosek license into)
via

```bash
docker run --name mosek -v $PWD/licenses:/usr/share/nginx/html:ro -p 8080:80 -d nginx
```

The license will now be exposed via http://localhost:8080

As an alternative you can run the script

```bash
./license_server.sh
```
