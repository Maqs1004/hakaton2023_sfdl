from flask import Flask, render_template, jsonify, request

import getting_data
import queries

app = Flask(__name__)


@app.route('/')
def main_page():
    directions = queries.direction_list()
    price_classes = queries.price_classes()
    return render_template('main.html', directions=directions, price_classes=price_classes)


@app.route('/getdata', methods=['POST'])
def getdata():
    request_data: dict = request.get_json()
    response_data = {}
    profile_flight = bool(request_data.get('profile_flight'))
    profile_saled = bool(request_data.get('profile_saled'))
    seasons = bool(request_data.get('seasons'))
    dynamics = bool(request_data.get('dynamics'))
    if profile_flight:
        response_data['profile_flight_block'] = getting_data.get_profile_flight(request_data)
    if profile_saled:
        response_data['profile_saled_block'] = getting_data.get_profile_saled(request_data)
    if seasons:
        response_data['seasons_block'] = getting_data.get_seasons(request_data)
    if dynamics:
        response_data['dynamics_block'] = getting_data.get_dynamics(request_data)
    return jsonify(response_data)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", port=80, debug=True)
