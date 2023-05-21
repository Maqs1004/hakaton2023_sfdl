from flask import Flask, render_template

import queries

app = Flask(__name__)


@app.route('/')
def main_page():
    directions = queries.direction_list()
    return render_template('main.html', directions=directions)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", port=80, debug=True)
