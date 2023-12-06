#!/usr/bin/bash
#a Bash script that takes in a URL and displays the body of the response
curl -sX GET -H "X-School-User-Id: 98" "$1"
