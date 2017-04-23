import rotor.rotor


class RotorII(rotor.rotor.Rotor):

    wheel = {
        'a': 'a',
        'b': 'j',
        'c': 'd',
        'd': 'k',
        'e': 's',
        'f': 'i',
        'g': 'r',
        'h': 'u',
        'i': 'x',
        'j': 'b',
        'k': 'l',
        'l': 'h',
        'm': 'w',
        'n': 't',
        'o': 'm',
        'p': 'c',
        'q': 'q',
        'r': 'g',
        's': 'z',
        't': 'n',
        'u': 'p',
        'v': 'y',
        'w': 'f',
        'x': 'v',
        'y': 'o',
        'z': 'e',
    }

    def _shouldNextRotate(self, letter: str) -> bool:
        return letter == 'e'
