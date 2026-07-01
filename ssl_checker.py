import ssl
import socket
from datetime import datetime


def get_ssl_info(hostname):

    try:

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=10) as sock:

            with context.wrap_socket(sock, server_hostname=hostname) as secure_socket:

                certificate = secure_socket.getpeercert()

        issuer = dict(item[0] for item in certificate["issuer"])

        subject = dict(item[0] for item in certificate["subject"])

        valid_from = datetime.strptime(
            certificate["notBefore"],
            "%b %d %H:%M:%S %Y %Z"
        )

        valid_until = datetime.strptime(
            certificate["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        days_remaining = (valid_until - datetime.utcnow()).days

        return {

            "available": True,

            "issued_to": subject.get("commonName", "Unknown"),

            "issued_by": issuer.get("commonName", "Unknown"),

            "valid_from": valid_from.strftime("%d-%b-%Y"),

            "valid_until": valid_until.strftime("%d-%b-%Y"),

            "days_remaining": days_remaining

        }

    except Exception:

        return {

            "available": False

        }