#!/usr/bin/python3
"""Sends an email as a POST parameter and displays the response."""
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    with request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
