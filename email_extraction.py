#!/usr/local/bin/python3

import colored
import re

print(colored.stylize("\n---- | Extract email out of text | ----\n", colored.fg("red")))

"""
A sample usage of regular expression
"""

message = input("Import text: ")

# basis for building our regex
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\-]+)"

"""
[\w\.-]+ <== matches one or more word character, dot or dash
"""

match = re.search(pattern, message)

if match:
    colored_match = colored.stylize(match.group(), colored.fg("red"))
    print(f"\nEmail found in text:\n>>> {colored_match}\n")
else:
    print("\nThere is no email in this text.\n")
