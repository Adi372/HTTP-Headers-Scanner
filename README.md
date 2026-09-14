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

## Security Headers Checked

The scanner currently checks:

* `Strict-Transport-Security`
* `Content-Security-Policy`
* `X-Content-Type-Options`
* `X-Frame-Options`
* `Referrer-Policy`
* `Permissions-Policy`


## Security Headers Detailed Description

### 1. `Strict-Transport-Security` (HSTS)

> "Always use HTTPS when connecting to me."

Example:

```text
Strict-Transport-Security: max-age=31536000
```

This tells the browser to remember for `31536000` seconds (1 year) that the website should only be accessed through HTTPS.

**Protects against:** HTTP downgrade / certain man-in-the-middle attacks.

---

### 2. `Content-Security-Policy` (CSP)

> "Only load scripts, images, styles, etc. from sources I allow."

Example:

```text
Content-Security-Policy: default-src 'self'
```

`'self'` means the browser should generally load resources only from the same website.

For example, if an attacker injects:

```html
<script src="https://evil.com/script.js"></script>
```

a restrictive CSP can tell the browser **not to load it**.

**Protects against:** Mainly XSS and malicious resource injection.

---

### 3. `X-Content-Type-Options`

> "Don't try to guess the type of this file."

Example:

```text
X-Content-Type-Options: nosniff
```

Suppose the server says:

```text
Content-Type: text/plain
```

The browser should respect that instead of trying to interpret the content as something else.

**Protects against:** MIME-type confusion / MIME sniffing attacks.

---

### 4. `X-Frame-Options`

> "Don't allow other websites to put my page inside a frame."

Example:

```text
X-Frame-Options: DENY
```

Imagine an attacker creates:

```html
<iframe src="https://bank.com"></iframe>
```

`DENY` tells the browser that `bank.com` should **not be displayed inside a frame**.

**Protects against:** Clickjacking.

Common values:

```text
DENY
SAMEORIGIN
```

* `DENY` → don't allow framing anywhere
* `SAMEORIGIN` → allow framing only by the same origin

---

### 5. `Referrer-Policy`

> "Control how much information about the previous URL is sent when navigating to another website."

Example:

```text
Referrer-Policy: strict-origin-when-cross-origin
```

Suppose you're visiting:

```text
https://example.com/account/settings
```

and click a link to:

```text
https://other-site.com
```

The browser may send referrer information.

The policy controls **how much of the original URL is shared**.

**Protects against:** Unnecessary URL/path information leaking to other websites.

---

### 6. `Permissions-Policy`

> "Control which browser features websites are allowed to use."

Example:

```text
Permissions-Policy: camera=(), microphone=()
```

This tells the browser:

```text
Camera     → not allowed
Microphone → not allowed
```

So even if some page tries to request access to the camera or microphone, the policy can prevent that feature from being used.

It can also control features such as:

```text
camera
microphone
geolocation
```

**Protects against:** Unnecessary or unwanted use of powerful browser features.

---

## Quick Summary of the Headers

| Header                     | Simple idea                    |
| -------------------------- | ------------------------------ |
| **HSTS**                   | HTTPS only                     |
| **CSP**                    | Only allow trusted resources   |
| **X-Content-Type-Options** | Don't guess file type          |
| **X-Frame-Options**        | Don't let others frame my site |
| **Referrer-Policy**        | Control URL information shared |
| **Permissions-Policy**     | Control browser features       |

---


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