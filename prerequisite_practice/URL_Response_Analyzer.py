import httpx
import sys


def analyze_url(url):
    try:
        response = httpx.get(url, timeout=5)
        print(f"Status code: {response.status_code}")
        print(f"Final URL: {response.url}")

        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print(f"Server: {response.headers.get('Server')}")

        if response.history:
            print("Redirected: Yes")
        else:
            print("Redirected: No")

    except httpx.TimeoutException:
        print("Error: Request timed out")

    except httpx.ConnectError:
        print("Error: Connection failed")

    except httpx.InvalidURL:
        print("Error: Invalid URL")

    except httpx.HTTPError:
        print("Error: HTTP error")

    except httpx.RequestError:
        print("Error: Request failed")


def main():
    url = sys.argv[1]
    analyze_url(url)

main()