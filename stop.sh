#!/usr/bin/env bash

if [[ "$0" != "${BASH_SOURCE[0]}" ]]; then
   export sourced="true"
   echo "sourced"
else 
   export sourced="false"
   echo "executed"
fi   

export project_dir="$(dirname ${0})"

cd ${project_dir}
echo "project_dir=$(pwd)}"

docker-compose -f greenbone-stack.yaml down 
