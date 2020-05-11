"""Module docstring."""
import json

from flask import Flask, abort, request

from .morse import Morse

app = Flask(__name__)


def get_string_from_file(post_request):
    """Get string from file in request."""
    # check if the post request has the file part
    if 'file' not in post_request.files:
        return None
    file = post_request.files['file']
    if file.filename == '':
        return None
    return file.read().decode('ascii').strip()


@app.route('/encode', methods=['POST'])
def encode():
    """Encode file contents from ASCII into Morse code."""
    text = get_string_from_file(request)
    if text is None:
        abort(400)
    result = {'result': Morse.ascii_to_morse(text)}
    return json.dumps(result)


@app.route('/decode', methods=['POST'])
def decode():
    """Decode file contents from Morse code into ASCII."""
    text = get_string_from_file(request)
    if text is None:
        abort(400)
    result = {'result': Morse.morse_to_ascii(text)}
    return json.dumps(result)


def main():
    """Start the program."""
    app.run()


if __name__ == '__main__':
    main()
