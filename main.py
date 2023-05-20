from flask import Flask, request, jsonify, render_template
import queries


app = Flask(__name__)



@app.route('/main')
def main_page():
    return render_template('dynamics.html')

# @app.route('/seasons')
# def seasons_page():
#     directions = queries.direction_list()
#     return render_template('seasons.html', directions=directions)
#
# @app.route('/dynamic')
# def dynamic_page():
#     directions = queries.direction_list()
#     return render_template('dynamic.html', directions=directions)
#
# @app.route('/profile')
# def profile_page():
#     directions = queries.direction_list()
#     return render_template('profile.html', directions=directions)



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", port=80, debug=True)
