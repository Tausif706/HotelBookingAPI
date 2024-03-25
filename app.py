from flask import Flask, request, jsonify
from main.list import listing
from flask_cors import CORS

from main.word import generate_word_frequency,append_to_output_file

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/list', methods=['POST'])
def create_list_terms():
    try:
        user_requirements = request.json.get('user_requirements')
        if not user_requirements:
            return jsonify({"error": "User requirements not provided"}), 400

        lists = listing(user_requirements)
        # print(lists)
        return jsonify(lists)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/store', methods=['POST'])
def store_new_hotel():
    try:
        # Assuming the request body is in JSON format
        data = request.json

        # Access the data fields sent from the React component
        title = data.get('title')
        description = data.get('description')
        if not description or not title:
            return jsonify({"error": "User requirements not provided"}), 400
        title_content = generate_word_frequency(title)
        append_to_output_file(title_content)
        description_content = generate_word_frequency(description)
        append_to_output_file(description_content)
        return jsonify(description_content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
