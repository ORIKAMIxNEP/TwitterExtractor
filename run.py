from flask import Flask, render_template, request
from flask_cors import CORS

from ExtractTwitter import ExtractTwitter

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)


@app.route("/", methods=["GET"])
def Web():
    return render_template("index.html")


@app.route("/extract_twitter", methods=["GET"])
def CallExtractTwitter():
    return ExtractTwitter(request.args.get("word"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
