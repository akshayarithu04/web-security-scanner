from flask import Flask
from flask import render_template
from flask import request
from database import create_database
from database import save_scan
from database import get_history
from flask import send_file
from report_generator import generate_pdf
from database import init_db

from scanner import scan_website

app = Flask(__name__)
init_db()

latest_report = None
@app.route("/")
def home():

    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    global latest_report

    url = request.form["url"]

    report = scan_website(url)

    save_scan(report)

    latest_report = report

    return render_template(
        "result.html",
        **report
    )
@app.route("/download")
def download():

    global latest_report

    if latest_report is None:

        return "No report available."

    pdf_file = generate_pdf(latest_report)

    return send_file(
        pdf_file,
        as_attachment=True
    )

@app.route("/history")
def history():

    scans = get_history()

    return render_template(

        "history.html",

        scans=scans

    )


if __name__ == "__main__":

    create_database()

    app.run(debug=True)