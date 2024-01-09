#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally
displays the body of the response.
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
