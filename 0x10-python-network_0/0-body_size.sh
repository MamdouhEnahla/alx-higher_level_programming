#!/bin/bash
# use curl to send request and display response size

url="$1"
size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')
echo $size
