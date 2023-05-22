#!/bin/bash

PORT=8080

docker run --name mosek -v $PWD/license:/usr/share/nginx/html:ro -p $PORT:80 -d nginx

echo "Nginx server running on port $PORT"
echo "Stop the server using 'docker rm -f mosek'"

