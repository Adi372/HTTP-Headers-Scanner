import httpx


HEADER_RULES = [
    {
        "header": "Strict-Transport-Security",
        "severity": "high",
        "recommendation": "Enable HSTS"
    },
    {
        "header": "Content-Security-Policy",
        "severity": "high",
        "recommendation": "Add a Content-Security-Policy"
    },
    {
        "header": "X-Content-Type-Options",
        "severity": "medium",
        "recommendation": "Set X-Content-Type-Options to nosniff"
    },
    {
        "header": "X-Frame-Options",
        "severity": "medium",
        "recommendation": "Set X-Frame-Options"
    },
    {
        "header": "Referrer-Policy",
        "severity": "low",
        "recommendation": "Set a Referrer-Policy"
    },
    {
        "header": "Permissions-Policy",
        "severity": "low",
        "recommendation": "Set a Permissions-Policy"
    }
]


def check_header(response, rule):
    header = rule["header"]
    value = response.headers.get(header)

    if value is not None:
        return {
            "header": header,
            "status": "present",
            "severity": rule["severity"],
            "value": value,
            "recommendation": rule["recommendation"]
        }

    return {
        "header": header,
        "status": "missing",
        "severity": rule["severity"],
        "value": None,
        "recommendation": rule["recommendation"]
    }


def scan_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = httpx.get(url, timeout=5)

        results = []

        for rule in HEADER_RULES:
            result = check_header(response, rule)
            results.append(result)

        return results

    except httpx.RequestError:
        return None


def print_report(url, results):
    print(f"\nURL: {url}")
    print("-" * 50)

    for result in results:
        if result["status"] == "present":
            print(
                f"[+] {result['header']}: Present "
                f"({result['severity']})"
            )
        else:
            print(
                f"[-] {result['header']}: Missing "
                f"({result['severity']})"
            )
            print(f"    Recommendation: {result['recommendation']}")


def main():
    url = input("Enter URL: ")

    results = scan_url(url)

    if results is None:
        print("Request failed")
        return

    print_report(url, results)


main()