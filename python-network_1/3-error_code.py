#!/usr/bin/python3
"""Fetches a URL and handles HTTP errors."""
from urllib import request
from urllib import error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
