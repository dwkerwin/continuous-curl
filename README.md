# Continuous cURL

Something I quickly threw together to continually test an endpoint over time, keeping track of http status codes.  Similar to ping -c but with curl.

## Usage

```shell
# python ccurl.py url.com times
python ccurl.py www.google.com 10
```
