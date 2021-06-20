#!/usr/bin/env bash
#

search_dir=/shared/watching_servers
new_dir=/shared/enroller/servers/

while :; do
  IFS=' ' read -ra files <<< $(ls $search_dir)
  for entry in ${files[@]}
  do
    echo "moving $entry"
    mv "$search_dir/$entry" $new_dir
  done
  sleep 3
done
