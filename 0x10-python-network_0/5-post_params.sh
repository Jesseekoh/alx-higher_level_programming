#!/bin/bash
# a script that sends a POST request to the passed URL, and show the body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
