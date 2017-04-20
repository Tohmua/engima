from typing import List
from rotor.rotor import Rotor
from rotor.rotor_i import RotorI
from rotor.rotor_ii import RotorII
from rotor.rotor_iii import RotorIII


def create(rotorSettings: dict) -> List[Rotor]:
    for rotorId, startingPosition in rotorSettings.items():
        return loadRotor(rotorId, startingPosition)


def loadRotor(rotorId: str, startingPosition: int):
    try:
        rotorsModule = __import__('rotor')

        rotorModule = getattr(
            rotorsModule,
            'rotor_{}'.format(rotorId).lower()
        )

        rotorClass = getattr(
            rotorModule,
            'Rotor{}'.format(rotorId)
        )

        return rotorClass(startingPosition)

    except AttributeError as error:
        raise Exception(
            'Rotor {} does not exist, please check your configuration'
            .format(rotorId)
        )
