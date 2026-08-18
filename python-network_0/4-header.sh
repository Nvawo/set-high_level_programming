#!/bin/bash
# Sends a GET request with the required X-School-User-Id header and displays the response body.
curl -s -H "X-School-User-Id: 98" "$1"
