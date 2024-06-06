#!/bin/bash
# use curl to send request and display response size
curl -s "$1" | wc -c
