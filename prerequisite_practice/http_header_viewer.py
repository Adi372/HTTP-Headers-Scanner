import httpx
import sys

url = sys.argv[1]

try:
    response = httpx.get(url)
    print(f"Status: {response.status_code}")

    if "--header" in sys.argv:
        index = sys.argv.index("--header")

        if index + 1 < len(sys.argv):
            header_name = sys.argv[index + 1]

            value = response.headers.get(header_name)

            if value is not None:
                print(f"{header_name}: {value}")
            else:
                print(f"Header not found: {header_name}")

    else:
        print("Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

except httpx.RequestError:
    print("Request Failed")