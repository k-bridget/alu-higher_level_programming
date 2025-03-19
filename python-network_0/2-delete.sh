#!/bin/bash
# sends DELETE request to $1 URL and display the body of the response
curl -s "$1" -X DELETE
