"""Unit tests module."""
from dbg_assignment_ignat.morse import Morse

test_tuple = (('t', '-'),
              ('T', '-'),
              ('Test', '- . ... -'),
              ('t e', '-  .'),
              )


def test_ascii_to_morse():
    for element in test_tuple:
        assert Morse.ascii_to_morse(element[0]) == element[1]


def test_morse_to_ascii():
    for element in test_tuple:
        assert Morse.morse_to_ascii(element[1]) == element[0].upper()
