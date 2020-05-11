"""Module for converting between ASCII and Morse code."""


class Morse:
    """Class to handle Morse code."""

    morse_set = (
        ('A', '.-'),
        ('B', '-...'),
        ('C', '-.-.'),
        ('D', '-..'),
        ('E', '.'),
        ('F', '..-.'),
        ('G', '--.'),
        ('H', '....'),
        ('I', '..'),
        ('J', '.---'),
        ('K', '-.-'),
        ('L', '.-..'),
        ('M', '--'),
        ('N', '-.'),
        ('O', '---'),
        ('P', '.--.'),
        ('Q', '--.-'),
        ('R', '.-.'),
        ('S', '...'),
        ('T', '-'),
        ('U', '..-'),
        ('V', '...-'),
        ('W', '.--'),
        ('X', '-..-'),
        ('Y', '-.--'),
        ('Z', '--..'),
        ('1', '.----'),
        ('2', '..---'),
        ('3', '...--'),
        ('4', '....-'),
        ('5', '.....'),
        ('6', '-....'),
        ('7', '--...'),
        ('8', '---..'),
        ('9', '----.'),
        ('0', '-----'),
        ('.', '.-.-.-'),
        (',', '--..--'),
        ('?', '..--..'),
        (' ', '  '),
    )

    to_morse_dict = dict(morse_set)

    to_ascii_dict = dict(map(lambda x: (x[1], x[0]), morse_set))

    @classmethod
    def ascii_to_morse(cls, text):
        """Convert ASCII to Morse code."""
        txt = text.upper()

        result = ' '.join(map(lambda x: cls.to_morse_dict.get(x, '/').replace('  ', ''), txt))
        return result

    @classmethod
    def morse_to_ascii(cls, text):
        """Convert Morse code to ASCII."""
        symbols_list = text.replace('  ', ' * ').split()

        result = ''.join(map(lambda x: cls.to_ascii_dict.get(x.replace('*', '  '), '/'), symbols_list))
        return result
