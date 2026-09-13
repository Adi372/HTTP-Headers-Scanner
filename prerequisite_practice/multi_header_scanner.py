import httpx

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(response):
    count = 0
    for header in SECURITY_HEADERS:
        if response.headers.get(header) is not None:
            count += 1
    return count

def scan_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = httpx.get(url, timeout=5)
        count = check_headers(response)

        return count

    except httpx.RequestError:
        return None

def main():
    urls=[]
    length = int(input("How many URLs do u want to check: "))
    for i in range (length):
        url = input("Enter URL: ")
        urls.append(url)

    for url in urls:
        count = scan_url(url)

        if count is None:
            print(f"{url}: Request failed")
        else:
            print(f"{url}: {count}/6 headers")

main()