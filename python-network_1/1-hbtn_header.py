#!/usr/bin/python3
"""Fetches and displays the X-Request-Id response header."""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
