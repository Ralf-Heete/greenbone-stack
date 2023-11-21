#!/usr/bin/env bash

if [[ "$0" != "${BASH_SOURCE[0]}" ]]; then
   export sourced="true"
   echo "sourced"
else 
   export sourced="false"
   echo "executed"
fi   
export script_name="$(basename ${0})"
export project_dir="$(dirname ${0})"
echo "project_dir=${project_dir}"

# Defines the path to the Unix Socket
SYSLOG_SOCKET="./volumes/syslog_socket_vol/socket"

log_message() {
    local log_level=$1
    local message=$2

    # Checks if the socket exists
    if [[ -e  "$SYSLOG_SOCKET" ]]; then
       logger -u "$SYSLOG_SOCKET" -p "$log_level" -t "${script_name}" "$message"
    else 
       echo "${log_level}:${script_name}:${message}" 		    
    fi   
}

SYSLOG="gb_syslog"
cd $project_dir

if [[ ! -e "volumes/syslog_socket_vol/socket" ]]; then
   docker-compose -f greenbone-stack.yaml up "${SYSLOG}" -d
fi

counter=30

while [[ ! -e volumes/syslog_socket_vol/socket ]]; do
  if [[	$counter == 0 ]]; then
	  echo "Timeout reached, Syslog socket not available" 
	  exit 1
  fi	  
  echo "Waiting for syslog Socket..."
  sleep 1
  ((counter--))
done

# Only logs from the current session
docker exec $SYSLOG /opt/rsyslog/scripts/logrotate.sh || log_message "local.error" "logrotate failed"
 
#starting 
docker-compose -f greenbone-stack.yaml up -d #logs automatically

