import argparse
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", default=False)
    return parser.parse_args()

if __name__ == "__main__":
    args = handle_args()
    app.debug = args.debug
    app.run()
