import os
import sys
import time
import subprocess


print("Ccurl (Continuous Curl)")
if len(sys.argv) <= 1:
    print("USAGE: python ccurl.py url.com times")
    print("USAGE: python ccurl.py www.google.com 10")
    sys.exit(0)

url = sys.argv[1]
times = int(sys.argv[2])
if len(sys.argv) > 3:
    delay_seconds = int(sys.argv[3])
    print("Delay between requests: {} seconds".format(delay_seconds))
else:
    delay_seconds = 0

# format of command without python string interpolation making it weird
# curl -k url.com --write-out %{http_code} --silent --output /dev/null
cmd = "curl -k {} --write-out %{{http_code}} --silent --output /dev/null".format(url)
print(cmd)

ok_count = 0
total_count = 0
response_codes = {}
for idx in range(times):
    try:
        status_code = subprocess.check_output(cmd, shell=True)
        if not status_code in response_codes:
            response_codes[str(status_code)] = 1
        else:
            response_codes[str(status_code)] += 1
        print("{}{} (try {}) Status: {}, Accum: {}".format(
            url[0:20],
            '...' if len(url) > 20 else '',
            idx,
            status_code,
            response_codes))
        time.sleep(delay_seconds)
    except KeyboardInterrupt:
        sys.exit(1)
        break
