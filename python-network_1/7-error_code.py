#!/usr/bin/python3
"""Sends a request and displays the response or its HTTP error code."""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
