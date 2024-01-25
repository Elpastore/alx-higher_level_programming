#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -w %{http_code} -s --output /dev/null $1)
