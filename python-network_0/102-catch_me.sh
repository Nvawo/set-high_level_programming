#!/bin/bash
# Sends a PUT request and follows the redirect to display the server response.
curl -s -L -X PUT 0.0.0.0:5000/catch_me
