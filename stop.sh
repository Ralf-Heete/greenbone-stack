#!/bin/bash
cd /docker/greenbone/
docker-compose -f syslog.yaml down
docker-compose -f greenbone-stack.yaml down 
