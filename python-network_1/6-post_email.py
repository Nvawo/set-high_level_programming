#!/usr/bin/python3
"""Sends an email as a POST parameter and displays the response."""
import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
