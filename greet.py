import math
import sys
from os import rename

import requests


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("Tony"))
print(greet("Tai"))

r = requests.get("https://google.com")
print(r.status_code)
