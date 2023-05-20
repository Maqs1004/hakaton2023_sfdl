from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/seasons')
def seasons_page():
    return render_template('seasons.html')

@app.route('/dynamic')
def dynamic_page():
    return render_template('dynamic.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", port=80, debug=True)
