#!/bin/bash
# Send a request to a URL and display the size of the request
curl -s "$1" | grep "Content-Length" | cut -d' ' -f 2
