from flask import Flask, request, jsonify
from itertools import permutations
import datetime, json
import logging
from logging.handlers import RotatingFileHandler
import unscramble_words_function as uw

# Configure logging
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
handler = RotatingFileHandler("logs/logs.log", maxBytes=100 * 1024 * 1024, backupCount=5)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
log.addHandler(handler)

app = Flask(__name__)

@app.route('/update_dictionary', methods=['POST'])
def update_dictionary():
    # Read json request
    request_data = request.get_json()
    if (not request_data):
        request_data = request.get_data()
        request_data = json.loads(request_data)

    # Get current timestamp
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    global dictionary, dictionary_loaded

    # Extract file directories from request
    dictionary = request_data.get('dictionary')

    # Log the received request details
    log.info('Receive request for Dictionary Update with file "' + dictionary + '", "'+ 'with process date ' + now )

    try:

        dictionary_loaded = uw.load_dictionary(dictionary)

        return app.response_class(
                response = json.dumps({"response":"OK", "message":"Process completed"}),
                status = 200,
                mimetype = 'application/json'
            )
        
    except Exception as Error:
        # Log error and return failure response
        log.error('Process Failed.')
        log.exception(Error)
        return app.response_class(
            response = json.dumps({"response":"FAILED", "message":str(Error).replace("'", "")}),
            status = 403,
            mimetype = 'application/json'
        )
    

@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    if (not request_data):
        request_data = request.get_data()
        request_data = json.loads(request_data)

    # Get current timestamp
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Extract text from request
    text = request_data.get('text')

    # Log the received request details
    log.info('Receive request for Unscramble Words for "' + text + '" with process date ' + now )

    try:

        possible_words = uw.unscramble(text, dictionary_loaded)
        
        result = {}
        for word in possible_words:
            length = len(word)
            if length not in result:
                result[length] = []
            result[length].append(word)
        
        detailed_result = {}
        for length, words in result.items():
            detailed_result[f"found {len(words)} words for {length}-letters"] = words

        # Check if locations are detected
        if detailed_result:
            # Return success response with detected locations
            return app.response_class(
                response = json.dumps({"response":"OK", "message":"Process completed", 
                                       "payload":json.loads(json.dumps(detailed_result))}),
                status = 200,
                mimetype = 'application/json'
            )
        else:
            # Return success response with message if no locations are detected
            return app.response_class(
                response = json.dumps({"response":"OK", "message":"Words not detected in the text"}),
                status = 201,
                mimetype = 'application/json'
            )
        
    except Exception as Error:
        # Log error and return failure response
        log.error('Process Failed.')
        log.exception(Error)
        return app.response_class(
            response = json.dumps({"response":"FAILED", "message":str(Error).replace("'", "")}),
            status = 403,
            mimetype = 'application/json'
        )

if __name__ == '__main__':
    # Start the Flask application on localhost (127.0.0.1) with debug mode enabled and port 5000.
    app.run(debug=True, host='127.0.0.1', port=5001)