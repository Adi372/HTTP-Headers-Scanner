import httpx
import time

URL = input("Enter the url: ")

try:
    start = time.time()
    response = httpx.get(URL)
    end = time.time()
    response_time = end - start
    print(f"URL : {response.url}")
    print(f"Status: {response.status_code}")
    print(f"Response time: {response_time:.2f} s")

except httpx.RequestError:
    print("Request Failed")