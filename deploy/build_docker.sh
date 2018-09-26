#!/bin/bash

source m3u_parser.env

rm -rf app
mkdir app
cp -r ../src app/.
cp ../app.py app/
cp ../requirements.txt app/

#create docker image
docker build -t ${COMPONENT_NAME} .
