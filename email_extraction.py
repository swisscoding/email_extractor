#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

import colored, re

print(colored.stylize("\n---- | Extract email out of text | ----\n", colored.fg("red")))

# user interaction
message = input("Import text: ")

# basis for building the regex
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\-]+)"

"""
[\w\.-]+ <== matches one or more word character, dot or dash
"""

# search the pattern
match = re.search(pattern, message)

# output
if match:
    colored_match = colored.stylize(match.group(), colored.fg("red"))
    print(f"\nEmail found in text:\n>>> {colored_match}\n")
else:
    print("\nThere is no email in this text.\n")
