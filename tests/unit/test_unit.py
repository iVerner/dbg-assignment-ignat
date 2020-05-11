"""Unit tests module."""
from dbg_assignment_ignat.morse import Morse

test_tuple = (
    ('T', '-'),
    ('Test', '- . ... -'),
    ('t e', '-  .'),
)

test_to_morse = (
    ('t', '-'),
    ('^', '/'),
)

test_to_ascii = (
    ('/', '^'),
)


def test_ascii_to_morse():  # noqa: D103
    for element in test_tuple + test_to_morse:
        assert Morse.ascii_to_morse(element[0]) == element[1]


def test_morse_to_ascii():  # noqa: D103
    for element in test_tuple + test_to_ascii:
        assert Morse.morse_to_ascii(element[1]) == element[0].upper()
