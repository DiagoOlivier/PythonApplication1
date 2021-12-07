import sys
import math

# ------------Debut debugg----------
message ="C"
# ------------Stop Debug------------
# message = input()
message = ''.join(format(ord(c), 'b') for c in message)

print(message)