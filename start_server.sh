#!/bin/bash

echo "Exposing the license"
cat $PWD/web/mosek

PORT=8080

docker run --name mosek -v $PWD/web:/usr/share/nginx/html:ro -p $PORT:80 -d nginx

echo "Nginx server running on port $PORT"
echo "Stop the server using 'docker rm -f mosek'"
