from reflector.reflector import Reflector
from reflector.reflector_a import ReflectorA


def create(reflectorId: str) -> Reflector:

    try:
        reflectorsModule = __import__('reflector')

        reflectorModule = getattr(
            reflectorsModule,
            'reflector_{}'.format(reflectorId).lower()
        )

        reflectorClass = getattr(
            reflectorModule,
            'Reflector{}'.format(reflectorId)
        )

        return reflectorClass()

    except AttributeError as error:
        raise Exception(
            'Reflector {} does not exist, please check your configuration'
            .format(reflectorId)
        )
