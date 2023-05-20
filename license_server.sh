#!/bin/bash

docker run --name mosek -v $PWD/licenses:/usr/share/nginx/html:ro -p 8080:80 -d nginx
