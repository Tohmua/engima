import rotor.rotor


class RotorIII(rotor.rotor.Rotor):

    wheel = {
        'a': 'b',
        'b': 'd',
        'c': 'f',
        'd': 'h',
        'e': 'j',
        'f': 'l',
        'g': 'c',
        'h': 'p',
        'i': 'r',
        'j': 't',
        'k': 'x',
        'l': 'v',
        'm': 'z',
        'n': 'n',
        'o': 'y',
        'p': 'e',
        'q': 'i',
        'r': 'w',
        's': 'g',
        't': 'a',
        'u': 'k',
        'v': 'm',
        'w': 'u',
        'x': 's',
        'y': 'q',
        'z': 'o',
    }

    def shouldNextRotate(self, letter: str) -> bool:
        if letter == 'w':
            return True

        return False
