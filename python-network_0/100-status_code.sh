#!/bin/bash
# sends a request to a URL, displays response status code only
curl -s -o /dev/null -w "%{http_code}" "$1"
