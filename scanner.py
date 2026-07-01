import requests
import socket
import time
from ssl_checker import get_ssl_info
from technology_detector import detect_technologies


def scan_website(url):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    start_time = time.time()

    response = requests.get(url, timeout=10)

    end_time = time.time()

    response_time = round((end_time - start_time) * 1000, 2)



    headers = response.headers
    technologies = detect_technologies(response)


    hostname = url.replace(
        "https://", ""
    ).replace(
        "http://", ""
    ).split("/")[0]

    ssl_info = get_ssl_info(hostname)

    ip_address = socket.gethostbyname(hostname)



    https = url.startswith("https://")


    security_headers = {

        "Content-Security-Policy":

            "Present"

            if "Content-Security-Policy" in headers

            else "Missing",

        "Strict-Transport-Security":

            "Present"

            if "Strict-Transport-Security" in headers

            else "Missing",

        "X-Frame-Options":

            "Present"

            if "X-Frame-Options" in headers

            else "Missing",

        "X-Content-Type-Options":

            "Present"

            if "X-Content-Type-Options" in headers

            else "Missing"

    }



    score = 100

    for value in security_headers.values():

        if value == "Missing":

            score -= 20

    if not https:

        score -= 20

    if score < 0:

        score = 0



    if score >= 80:

        risk = "Low"

    elif score >= 50:

        risk = "Medium"

    else:

        risk = "High"


    return {

    "url": url,

    "status": response.status_code,

    "server": headers.get("Server", "Hidden"),

    "ip": ip_address,

    "https": https,

    "security_headers": security_headers,

    "response_time": response_time,

    "score": score,

    "risk": risk,

    "ssl": ssl_info,

    "technologies": technologies

}