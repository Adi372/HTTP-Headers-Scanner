import httpx
import sys

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_security_headers(headers):
    for header in SECURITY_HEADERS:
        value = headers.get(header)

    if value is not None:
        print(f"[+] {header}: Present")
    else:
        print(f"[-] {header}: Missing")

def main():
    url = sys.argv[1]

    try:
        response = httpx.get(url)
        print(f"URL: {response.url}")
        print(f"Status: {response.status_code}")
        print()

        check_security_headers(response.headers)
    except httpx.RequestError:
        print("Request Failed")

main()
