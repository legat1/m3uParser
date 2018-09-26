#!/bin/bash

source m3u_parser.env

docker save -o ./${COMPONENT_NAME}.tar ${COMPONENT_NAME}
scp ./${COMPONENT_NAME}.tar sandbox:/home/ec2-user/${COMPONENT_NAME}/${COMPONENT_NAME}.tar
ssh sandbox sudo docker load -i /home/ec2-user/${COMPONENT_NAME}/${COMPONENT_NAME}.tar