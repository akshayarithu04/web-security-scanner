def detect_technologies(response):

    technologies = []

    headers = response.headers
    html = response.text.lower()

    # -----------------------
    # Server Detection
    # -----------------------

    server = headers.get("Server", "").lower()

    if "nginx" in server:
        technologies.append("Nginx")

    if "apache" in server:
        technologies.append("Apache")

    if "iis" in server:
        technologies.append("Microsoft IIS")

    if "cloudflare" in server:
        technologies.append("Cloudflare")

    # -----------------------
    # HTML Detection
    # -----------------------

    if "bootstrap" in html:
        technologies.append("Bootstrap")

    if "jquery" in html:
        technologies.append("jQuery")

    if "react" in html:
        technologies.append("React")

    if "angular" in html:
        technologies.append("Angular")

    if "vue" in html:
        technologies.append("Vue.js")

    if "wordpress" in html:
        technologies.append("WordPress")

    if "wp-content" in html:
        technologies.append("WordPress")

    if "php" in html:
        technologies.append("PHP")

    return sorted(list(set(technologies)))