import sys
try:
    from flask import Flask
    from flask import render_template
except ImportError:
    sys.stderr.write("Could not import Flask module. Is it installed? If so, does a virtual environment need to be activated? (e.g. venv/bin/activate_this.py)\n")
    sys.exit(1)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

def handle_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", default=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = handle_args()
    app.debug = args.debug
    app.run()
