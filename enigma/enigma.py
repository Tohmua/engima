from plugboard.plugboard import PlugBoard
from rotor.rotor import Rotor
from reflector.reflector import Reflector
from typing import List


class Enigma(object):
    plugboard = None
    rotors = []
    reflector = None

    def __init__(
        self,
        plugboard: PlugBoard,
        rotors: List[Rotor],
        reflector: Reflector
    ):
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector

    def encode(self, letter: str) -> str:
        letter = self.plugboard.parse(letter)

        letter = self.parseForwardThroughRotors(letter)

        letter = self.reflector.parse(letter)

        letter = self.parseBackwardThroughRotors(letter)

        letter = self.plugboard.parse(letter)

        return letter

    def parseForwardThroughRotors(self, letter: str) -> str:
        # The first rotor always rotates
        shouldRotateRotor = True

        for rotor in self.rotors:
            if shouldRotateRotor:
                rotor.rotate()

            shouldRotateRotor = rotor.shouldNextRotate(letter)
            letter = rotor.forward(letter)

        return letter

    def parseBackwardThroughRotors(self, letter: str) -> str:
        for rotor in reversed(self.rotors):
            letter = rotor.backward(letter)

        return letter
