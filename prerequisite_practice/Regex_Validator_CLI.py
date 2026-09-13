import re
import sys

def validate_hsts(value):
    pattern = r"max-age=\s*[1-9][0-9]"

    if re.search(pattern, value, re.IGNORECASE):
        return True

    return False

def main():
    value = sys.argv[1]
    if validate_hsts(value):
        print("Valid HSTS max-age")
    else:
        print("Invalid HSTS max-age")

main()