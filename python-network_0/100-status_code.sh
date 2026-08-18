#!/bin/bash
# Displays only the HTTP status code returned by the given URL.
curl -s -o /dev/null -w '%{http_code}' "$1"
