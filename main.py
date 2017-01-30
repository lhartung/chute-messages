from __future__ import print_function

import sys
import time

while True:
    print("log message")
    print("error message", file=sys.stderr)
    time.sleep(60)
