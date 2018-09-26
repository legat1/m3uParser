#!/bin/bash
source m3u_parser.env
docker stop ${COMPONENT_NAME} && docker wait ${COMPONENT_NAME} && docker rm -f ${COMPONENT_NAME}
docker run -p 1785:1785 -d --name ${COMPONENT_NAME} ${COMPONENT_NAME}

