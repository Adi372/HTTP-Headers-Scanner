import httpx
import sys
import re

SEVERITY_POINTS = {
    "high": 30,
    "medium": 15,
    "low": 5
}

HEADER_RULES = [
    {
        "header": "Strict-Transport-Security",
        "severity": "high",
        "recommendation": "Enable HSTS with a suitable max-age.",
    },
    {
        "header": "Content-Security-Policy",
        "severity": "high",
        "recommendation": "Add a Content-Security-Policy.",
    },
    {
        "header": "X-Content-Type-Options",
        "severity": "medium",
        "recommendation": "Set X-Content-Type-Options to nosniff.",
    },
    {
        "header": "X-Frame-Options",
        "severity": "medium",
        "recommendation": "Set X-Frame-Options.",
    },
    {
        "header": "Referrer-Policy",
        "severity": "low",
        "recommendation": "Set a suitable Referrer-Policy.",
    },
    {
        "header": "Permissions-Policy",
        "severity": "low",
        "recommendation": "Set a suitable Permissions-Policy.",
    }
]

def validate_header(header, value):
    if header == "Strict-Transport-Security":
        pattern = r"max-age=\s*[1-9][0-9]*"

        if re.search(pattern, value, re.IGNORECASE):
            return "OK"

        return "WEAK"

    if header == "X-Content-Type-Options":
        if value.lower().strip() == "nosniff":
            return "OK"

        return "WEAK"

    if header == "X-Frame-Options":
        if value.lower().strip() in ["deny", "sameorigin"]:
            return "OK"

        return "WEAK"

    if header == "Content-Security-Policy":
        if value.strip():
            return "OK"

        return "WEAK"

    if header == "Referrer-Policy":
        if value.strip():
            return "OK"

        return "WEAK"

    if header == "Permissions-Policy":
        if value.strip():
            return "OK"

        return "WEAK"

    return "WEAK"
    

def check_header(response, rule):
    header = rule["header"]
    severity = rule["severity"]
    recommendation = rule["recommendation"]

    value = response.headers.get(header)

    if value is None:
        return {
            "header": header,
            "severity": severity,
            "status": "MISSING",
            "value": value,
            "recommendation": recommendation
        }

    status = validate_header(header, value)

    return {
        "header": header,
        "severity": severity,
        "status": status,
        "value": value,
        "recommendation": recommendation
    }

def scan_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = httpx.get(url, timeout=5)
        findings = []
        for rule in HEADER_RULES:
            finding = check_header(response, rule)
            findings.append(finding)

        return response, findings

    except httpx.InvalidURL:
        print("Error: Invalid URL")

    except httpx.TimeoutException:
        print("Error: Request timed out")

    except httpx.ConnectError:
        print("Error: Connection Failed")

    except httpx.RequestError:
        print("Error: Request Failed")

    return None

def calculate_score(findings):
    total = 0
    earned = 0

    for finding in findings:
        severity = finding["severity"]
        status = finding["status"]

        points = SEVERITY_POINTS[severity]

        total += points

        if status == "OK":
            earned += points
        elif status == "WEAK":
            earned += points * 0.5
        elif status == "MISSING":
            earned += 0

    score = (earned/total) * 100

    return total, score, earned

def get_grade(score):
    if score >= 90:
        return "A"

    elif score >= 75:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 50:
        return "D"

    else:
        return "F"


def print_report(response, findings):
    total, earned, score = calculate_score(findings)
    grade = get_grade(score)

    print()
    print("=" * 60)
    print("HTTP SECURITY HEADERS SCANNER")
    print("=" * 60)

    print(f"URL: {response.url}")
    print(f"Status: {response.status_code}")

    if response.history:
        print(f"Redirects: {len(response.history)}")
    else:
        print("Redirects: 0")

    print()
    print("SECURITY HEADERS")
    print("-" * 60)

    for finding in findings:
        header = finding["header"]
        status = finding["status"]
        severity = finding["severity"]
        value = finding["value"]

        if status == "OK":
            print(f"[+] {header}")
            print(f"    Status: {status}")
            print(f"    Severity: {severity}")
            print(f"    Value: {value}")

        elif status == "WEAK":
            print(f"[!] {header}")
            print(f"    Status: {status}")
            print(f"    Severity: {severity}")
            print(f"    Value: {value}")
            print(f"    Recommendation: {finding['recommendation']}")

        else:
            print(f"[-] {header}")
            print(f"    Status: {status}")
            print(f"    Severity: {severity}")
            print(f"    Recommendation: {finding['recommendation']}")

        print()

    print("SCORE")
    print("-" * 60)
    print(f"Total: {total}")
    print(f"Earned: {earned}")
    print(f"Score: {score:.0f}")
    print(f"Grade: {grade}")


def main():
    url = sys.argv[1]
    response, findings = scan_url(url)

    if response is None:
        return 

    print_report(response, findings)
    

main()