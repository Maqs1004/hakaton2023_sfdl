from flask import Flask, render_template, jsonify, request

import queries

app = Flask(__name__)


@app.route('/')
def main_page():
    directions = queries.direction_list()
    return render_template('main.html', directions=directions)


@app.route('/getdata', methods=['POST'])
def getdata():
    """Пример входящего JSON
    {'direction': 'Москва - Сочи',
     'flight': 'Москва - Сочи',
     'class': 'Первый',
     'choose_date': '05/10/2023',
     'start': '',
     'finish': '',
     'dynamics': 'on',
     'seasons': 'on',
     'profile_flight': 'on',
     'profile_saled': 'on'}"""

    request_data: dict = request.get_json()
    response_data = {}
    profile_flight = bool(request_data.get('profile_flight'))
    profile_saled = bool(request_data.get('profile_saled'))
    seasons = bool(request_data.get('seasons'))
    dynamics = bool(request_data.get('dynamics'))
    if profile_flight:
        response_data['profile_flight_block'] = queries.get_profile_flight(request_data)
    if profile_saled:
        response_data['profile_saled_block'] = queries.get_profile_saled(request_data)
    if seasons:
        response_data['seasons_block'] = queries.get_seasons(request_data)
    if dynamics:
        response_data['dynamics_block'] = queries.get_dynamics(request_data)
    print(response_data)
    return jsonify(response_data)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", port=80, debug=True)
