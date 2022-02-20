#!/bin/sh
# This script stops the current database and rebuilds to give clean one
# run with sudo if you need to restart

docker-compose down --volumes
docker-compose up
