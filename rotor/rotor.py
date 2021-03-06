from abc import ABCMeta, abstractmethod


class Rotor(object):
    __metaclass__ = ABCMeta

    wheel = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'i': 'i',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'n': 'n',
        'o': 'o',
        'p': 'p',
        'q': 'q',
        'r': 'r',
        's': 's',
        't': 't',
        'u': 'u',
        'v': 'v',
        'w': 'w',
        'x': 'x',
        'y': 'y',
        'z': 'z',
    }

    should_next_rotate = False

    def __init__(self, startingPosition: int = 1):
        for i in range(1, startingPosition):
            self.rotate()

    @abstractmethod
    def _shouldNextRotate(self, letter: str) -> bool:
        pass

    def shouldNextRotate(self) -> bool:
        return self.should_next_rotate

    def rotate(self):
        self.should_next_rotate = False
        current = ''
        previous = ''
        first = ''
        rotatedRotor = {}

        for k, v in self.wheel.items():
            previous = current
            current = k

            if previous == '':
                first = current
                self.shouldNextRotate = self._shouldNextRotate(current)
                continue

            rotatedRotor.update({previous: v})

        rotatedRotor.update({current: self.wheel.get(first)})

        self.wheel.update(rotatedRotor)

    def forward(self, letter: str) -> str:
        if letter in self.wheel.keys():
            return self.wheel.get(letter)
        else:
            raise Exception('Letter {} not in rotor'.format(letter))

    def backward(self, letter: str) -> str:
        for k, v in self.wheel.items():
            if v == letter:
                return k

        raise Exception('Letter {} not in rotor'.format(letter))
