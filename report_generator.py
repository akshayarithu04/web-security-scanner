from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generate_pdf(report):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>WEB SECURITY SCANNER REPORT</b>", styles["Title"])
    )

    story.append(Spacer(1, 12))

    story.append(Paragraph(f"<b>Website:</b> {report['url']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>IP Address:</b> {report['ip']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Status Code:</b> {report['status']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Server:</b> {report['server']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>HTTPS:</b> {'Enabled' if report['https'] else 'Disabled'}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Response Time:</b> {report['response_time']} ms", styles["BodyText"]))

    story.append(Spacer(1, 12))

    story.append(
        Paragraph("<b>Security Headers</b>", styles["Heading2"])
    )

    for header, status in report["security_headers"].items():

        story.append(
            Paragraph(f"{header} : {status}", styles["BodyText"])
        )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph("<b>Risk Assessment</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(f"Security Score : {report['score']}/100", styles["BodyText"])
    )

    story.append(
        Paragraph(f"Risk Level : {report['risk']}", styles["BodyText"])
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph("<b>SSL Certificate</b>", styles["Heading2"])
    )

    if report["ssl"]["available"]:

        story.append(
            Paragraph(f"Issued To : {report['ssl']['issued_to']}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"Issued By : {report['ssl']['issued_by']}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"Valid Until : {report['ssl']['valid_until']}", styles["BodyText"])
        )

    else:

        story.append(
            Paragraph("SSL Certificate Not Available", styles["BodyText"])
        )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph("<b>Technologies Detected</b>", styles["Heading2"])
    )

    if report["technologies"]:

        for tech in report["technologies"]:

            story.append(
                Paragraph(f"• {tech}", styles["BodyText"])
            )

    else:

        story.append(
            Paragraph("No technologies detected.", styles["BodyText"])
        )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d-%b-%Y %H:%M:%S')}",
            styles["Italic"]
        )
    )

    doc.build(story)

    return filename