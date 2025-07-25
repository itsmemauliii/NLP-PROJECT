
from flask import Flask, render_template, request, jsonify
from utils.listing_logic import match_properties

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_input = request.json.get('query')
    results = match_properties(user_input)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
