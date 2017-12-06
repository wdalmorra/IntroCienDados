#!/bin/bash
counter=0
while IFS='' read -r line || [[ -n "$line" ]]; do
    wget "http://steamspy.com/api.php?request=appdetails&appid=$line"
    counter=$((counter+1))
    echo "$counter"
    # if [[ "$counter" -eq 200 ]]; then
    # 	counter=0
    # 	sleep 301
    # fi
done < "$1"