from flask import Flask, render_template, jsonify, request

import queries

app = Flask(__name__)


@app.route('/')
def main_page():
    directions = queries.direction_list()
    return render_template('main.html', directions=directions)


@app.route('/getdata', methods=['POST'])
def getdata():
    print(request.get_json())
    return jsonify({'data': 'OK'})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", port=80, debug=True)
