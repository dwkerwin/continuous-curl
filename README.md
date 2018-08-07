# Continuous cURL

Continually test an endpoint over time, keeping track of http status codes.  Similar to ping -c but with curl.

Forgive the lack of argparse, setup.py, etc.  This was thrown together quickly.

## Usage

```shell
# python ccurl.py url.com times optional_delay_between_seconds

# GET request on www.google.com 10 times
python ccurl.py www.google.com 10

# GET request on www.google.com 100 times with a 2 second sleep between requests
python ccurl.py www.google.com 100 2
```
