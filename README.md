# HTTP Security Headers Scanner

A small Python tool that checks a website's HTTP security headers and gives a basic security score.

I built this project to practice Python, HTTP requests, error handling, regular expressions, dictionaries, loops, and conditional logic while learning web security.

## Features

* Check HTTP security headers
* Detect missing headers
* Check basic header values
* Assign severity to each finding
* Calculate a security score
* Generate a security grade
* Follow redirects
* Handle common request errors

## Security Headers Checked

The scanner currently checks:

* `Strict-Transport-Security`
* `Content-Security-Policy`
* `X-Content-Type-Options`
* `X-Frame-Options`
* `Referrer-Policy`
* `Permissions-Policy`

Each finding can have one of three statuses:

```text
OK       → 100% of points
WEAK     → 50% of points
MISSING  → 0% of points
```

## Severity Points

```text
High     → 30 points
Medium   → 15 points
Low      → 5 points
```

The final score is calculated from the points earned compared to the total possible points.

## Requirements

* Python 3
* `httpx`

Install `httpx`:

```bash
pip install httpx
```

## Usage

Run the scanner with a URL:

```bash
python http_headers_scanner.py https://example.com
```

Example output:

```text
============================================================
HTTP SECURITY HEADERS SCANNER
============================================================
URL: https://example.com/
Status: 200
Redirects: 0

SECURITY HEADERS
------------------------------------------------------------
[-] Strict-Transport-Security
    Status: MISSING
    Severity: high
    Recommendation: Enable HSTS with a suitable max-age.

[+] X-Content-Type-Options
    Status: OK
    Severity: medium
    Value: nosniff

SCORE
------------------------------------------------------------
Total: 100
Earned: 40
Score: 40
Grade: F
```

## Error Handling

The scanner handles common request problems such as:

* Invalid URL
* Connection failure
* Timeout
* Other request errors

Example:

```text
Error: Request timed out
```

## Project Structure

```text
http_headers_scanner/
│
└── http_headers_scanner.py
```

## What I Practiced

This project combines concepts from my previous mini projects:

* HTTP requests with `httpx`
* HTTP response handling
* HTTP headers
* Dictionaries and lists
* Functions
* Loops
* Conditional logic
* Regular expressions
* Exception handling
* Redirect handling
* Basic security scoring

## Limitations

This is a learning project, not a full security auditing tool.

A header being present does not always mean it is configured securely. The current scanner only performs basic validation for some headers.


## Learning Goal

The main goal of this project was to understand how HTTP responses can be inspected and how simple security checks can be automated using Python.