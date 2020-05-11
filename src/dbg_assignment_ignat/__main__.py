"""Module docstring."""
import json

from flask import Flask, request

from .morse import Morse

app = Flask(__name__)


def get_string_from_file(request):
    # check if the post request has the file part
    if 'file' not in request.files:
        return None
    file = request.files['file']
    if file.filename == '':
        return None
    return file.read().decode('ascii').strip()


@app.route('/encode', methods=['POST'])
def encode():
    text = get_string_from_file(request)

    result = {'result': Morse.ascii_to_morse(text)}
    return json.dumps(result)


@app.route('/decode', methods=['POST'])
def decode():
    text = get_string_from_file(request)

    result = {'result': Morse.morse_to_ascii(text)}
    return json.dumps(result)


def main():
    """Start the program."""
    app.run()


if __name__ == '__main__':
    main()
