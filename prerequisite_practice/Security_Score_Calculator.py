SEVERITY_POINTS = {
    "high": 30,
    "medium": 15,
    "low": 5
}

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
            earned += points*0.5
        elif status == "MISSING":
            earned += 0

    score = (earned/total) * 100
    return total, earned, score

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


def main():
    findings = [
        {
            "header": "Strict-Transport-Security",
            "severity": "high",
            "status": "OK"
        },
        {
            "header": "Content-Security-Policy",
            "severity": "high",
            "status": "WEAK"
        },
        {
            "header": "X-Content-Type-Options",
            "severity": "medium",
            "status": "OK"
        },
        {
            "header": "X-Frame-Options",
            "severity": "medium",
            "status": "MISSING"
        },
        {
            "header": "Referrer-Policy",
            "severity": "low",
            "status": "OK"
        },
        {
            "header": "Permissions-Policy",
            "severity": "low",
            "status": "MISSING"
        }
    ]

    total, earned, score = calculate_score(findings)
    print(f"Total: {total}")
    print(f"Earned: {earned}")
    print(f"Score: {score:.0f}")
    print(f"Grade: {get_grade(score)}")


main()