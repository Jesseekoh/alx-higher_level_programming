#!/bin/bash
# a bash script that display all HTTP methods the server will accept
allowed_methods=$(curl -s -I -X OPTIONS <server_url> | grep -i "Allow" | cut -d' ' -f2-)
echo "Allowed HTTP methods: $allowed_methods"
