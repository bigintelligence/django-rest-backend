#!/bin/sh
set -e
shift
# wait for the postgres docker to be running
while :
do
  # shellcheck disable=SC2046
  i=$(python pgconnectcheck.py -db $PG_BASE -u $PG_USER -hs $PG_HOST -pw $PG_PASS -p $PG_PORT)
  >&2 echo $i
  if [ $i -eq 1 ]; then
    break
  fi
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 3
done

>&2 echo "Postgres is up - executing command"
exec "$@"

