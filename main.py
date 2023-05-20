from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", port=80, debug=True)
