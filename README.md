# 🛡️ Automated Web Vulnerability Scanner

A Flask-based automated web security scanner that analyzes websites for common security weaknesses and generates a detailed security assessment report.

The project performs security header analysis, SSL certificate validation, HTTPS verification, technology fingerprinting, risk scoring, and generates downloadable PDF security reports.

---

## 🚀 Live Demo

🔗 **Live Application:**  
https://web-security-scanner-1-duxp.onrender.com

---

## 📌 Project Overview

The Automated Web Vulnerability Scanner is a cybersecurity tool developed using Python and Flask that helps identify basic security misconfigurations in websites.

It performs automated reconnaissance and security checks similar to the initial stages of a vulnerability assessment process.

---

# ✨ Features

## 🔍 Website Security Analysis

- Website availability checking
- HTTP status code detection
- Response time measurement
- IP address lookup
- Server information detection


## 🔐 Security Header Analysis

Checks important HTTP security headers:

- Content-Security-Policy
- X-Frame-Options
- Strict-Transport-Security
- X-Content-Type-Options


## 🌐 SSL/TLS Certificate Analysis

- SSL certificate validation
- Certificate issuer detection
- Certificate expiry information
- Remaining validity days


## 🧩 Technology Detection

Detects web technologies used by the target website:

- Web servers
- Frameworks
- Frontend libraries
- CMS technologies


## 📊 Risk Assessment

Generates a security score based on detected issues:

- Low Risk
- Medium Risk
- High Risk


## 📄 Automated PDF Reports

Generates professional security assessment reports containing:

- Website details
- Security findings
- Risk score
- SSL information
- Technology details


## 📚 Scan History

Stores previous scans using SQLite database.
