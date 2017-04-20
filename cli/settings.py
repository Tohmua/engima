import configparser
from typing import List


class Settings(object):

    plugboard = {}
    rotors = []
    reflector = ''

    def __init__(self, filePath: str):
        config = configparser.ConfigParser()
        config.read(filePath)

        self.plugboard = self._getPlugboardSettings(config)
        self.rotors = self._getRotors(
            self._getRotorsIds(config),
            self._getRotorsSettings(config)
        )
        self.reflector = self._getReflector(config)

    def _getPlugboardSettings(self, config: configparser) -> dict:
        try:
            return dict(
                wiring[1].split(',') for wiring in config.items('plugboard')
            )

        except ValueError as error:
            raise Exception('Unable to parse plugboard configuration')

    def _getRotorsIds(self, config: configparser) -> dict:
        try:
            return dict(
                rotor for rotor in config.items('rotors')
            )
        except ValueError as error:
            raise Exception('Unable to parse rotors configuration')

    def _getRotorsSettings(self, config: configparser) -> dict:
        try:
            return dict(
                rotor_position for rotor_position in
                config.items('rotor_positions')
            )
        except ValueError as error:
            raise Exception('Unable to parse rotor_positions configuration')

    def _getReflector(self, config: configparser) -> str:
        try:
            return config.get('reflector', 'reflector')
        except ValueError as error:
            raise Exception('Unable to parse reflector configuration')

    def _getRotors(self, rotorIds: dict, rotorPositions: dict) -> List[dict]:
        rotors = []

        for rotor in rotorIds.items():
            if not rotorPositions[rotor[0]]:
                raise Exception(
                    'Rotor {} is missing its starting position'
                    .format(rotor[0])
                )

            rotors.append({rotor[1]: int(rotorPositions[rotor[0]])})

        return rotors
