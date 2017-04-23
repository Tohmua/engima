import unittest
from machine.machine import Machine
from plugboard.plugboard import PlugBoard
from rotor.rotor_i import RotorI
from rotor.rotor_ii import RotorII
from rotor.rotor_iii import RotorIII
from reflector.reflector_a import ReflectorA


class TestMachine(unittest.TestCase):

    def getSingleRotorMachine(self, r1_startPosition: int = 1):
        return Machine(
            PlugBoard({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j'}),
            [RotorI(r1_startPosition)],
            ReflectorA()
        )

    def getBiRotorMachine(
        self,
        r1_startPosition: int = 1,
        r2_startPosition: int = 1
    ):
        return Machine(
            PlugBoard({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j'}),
            [RotorI(1), RotorII(1)],
            ReflectorA()
        )

    def getTriRotorMachine(
        self,
        r1_startPosition: int = 1,
        r2_startPosition: int = 1,
        r3_startPosition: int = 1
    ):
        return Machine(
            PlugBoard({'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j'}),
            [RotorI(1), RotorII(1), RotorIII(1)],
            ReflectorA()
        )

    def test_single_rotor(self):
        for r1_startPosition in range(26):
            # for each letter of the alphabet
            for i in range(ord('a'), ord('z') + 1):
                charictor = chr(i)

                encodeMachine = self.getSingleRotorMachine(r1_startPosition)
                decodeMachine = self.getSingleRotorMachine(r1_startPosition)

                letters = []

                # create an array of 26 of the same letter and then encode them
                for i in range(26):
                    letters.append(encodeMachine.encode(charictor))

                # using an enigma in the same initial state decode the letters
                # and check they match in the input
                for letter in letters:
                    self.assertEqual(decodeMachine.encode(letter), charictor)

    def test_bi_rotor(self):
        for r1_startPosition in range(26):
            for r2_startPosition in range(26):
                # for each letter of the alphabet
                for i in range(ord('a'), ord('z') + 1):
                    charictor = chr(i)

                    encodeMachine = self.getBiRotorMachine(
                        r1_startPosition,
                        r2_startPosition
                    )
                    decodeMachine = self.getBiRotorMachine(
                        r1_startPosition,
                        r2_startPosition
                    )

                    letters = []

                    # create an array of 26 of the same letter and
                    # then encode them
                    for i in range(26):
                        letters.append(encodeMachine.encode(charictor))

                    # using an enigma in the same initial state decode
                    # the letters and check they match in the input
                    for letter in letters:
                        self.assertEqual(
                            decodeMachine.encode(letter), charictor
                        )

    def test_tri_rotor(self):
        for r1_startPosition in range(26):
            for r2_startPosition in range(26):
                for r3_startPosition in range(26):
                    # for each letter of the alphabet
                    for i in range(ord('a'), ord('z') + 1):
                        charictor = chr(i)

                        encodeMachine = self.getTriRotorMachine(
                            r1_startPosition,
                            r2_startPosition,
                            r3_startPosition
                        )
                        decodeMachine = self.getTriRotorMachine(
                            r1_startPosition,
                            r2_startPosition,
                            r3_startPosition
                        )

                        letters = []

                        # create an array of 26 of the same letter
                        # and then encode them
                        for i in range(26):
                            letters.append(encodeMachine.encode(charictor))

                        # using an enigma in the same initial state
                        # decode the letters and check they match in the input
                        for letter in letters:
                            self.assertEqual(
                                decodeMachine.encode(letter), charictor
                            )


if __name__ == '__main__':
    unittest.main()
