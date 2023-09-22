#!/usr/bin/env bash
echo "$(dirname $0)"
echo "${BASH_SOURCE[0]}"
DIR=/docker/greenbone
SYSLOG="gb_syslog"
cd $DIR

if [ ! -e $DIR/volumes/syslog_socket_vol/socket ]
then
   docker-compose -f syslog.yaml up -d
fi

while [ ! -e $DIR/volumes/syslog_socket_vol/socket ]; do
  echo "Warte auf syslog Socket..."
  sleep 1
done
# Nur logs von der aktuellen Sitzung
docker exec $SYSLOG /opt/rsyslog/scripts/logrotate.sh
 
#starting 
docker-compose -f greenbone-stack.yaml up -d
