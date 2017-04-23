import rotor.rotor


class RotorI(rotor.rotor.Rotor):

    wheel = {
        'a': 'e',
        'b': 'k',
        'c': 'm',
        'd': 'f',
        'e': 'l',
        'f': 'g',
        'g': 'd',
        'h': 'q',
        'i': 'v',
        'j': 'z',
        'k': 'n',
        'l': 't',
        'm': 'o',
        'n': 'w',
        'o': 'y',
        'p': 'h',
        'q': 'x',
        'r': 'u',
        's': 's',
        't': 'p',
        'u': 'a',
        'v': 'i',
        'w': 'b',
        'x': 'r',
        'y': 'c',
        'z': 'j',
    }

    def _shouldNextRotate(self, letter: str) -> bool:
        return letter == 'q'
