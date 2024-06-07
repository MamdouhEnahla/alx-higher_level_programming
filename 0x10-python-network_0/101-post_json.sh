#!/bin/bash
# Sends a POST request to URL first argument, displays body of response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
