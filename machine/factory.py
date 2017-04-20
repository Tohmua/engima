from cli.settings import Settings
from plugboard.plugboard import PlugBoard
from machine.machine import Machine
from reflector.factory import create as reflectorfactory
from rotor.factory import create as rotorFactory


def create(settings: Settings) -> Machine:
    plugboard = PlugBoard(settings.plugboard)

    rotors = list(
        map(
            lambda x: rotorFactory(x),
            settings.rotors
        )
    )

    reflector = reflectorfactory(settings.reflector)

    return Machine(plugboard, rotors, reflector)
