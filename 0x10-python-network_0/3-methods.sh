#!/bin/bash
# Takes a URL and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
