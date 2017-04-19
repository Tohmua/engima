from argparse import ArgumentParser
from cli.settings import Settings
from plugboard.plugboard import PlugBoard
import reflector.factory as rf
# from logger.logger import Logger


def main():
    args = getCliArguments()

    settings = Settings(args.settings)

    plugboard = PlugBoard(settings.plugboard)
    print(plugboard)

    reflector = rf.create('A')
    print(reflector)



def getCliArguments():
    ap = ArgumentParser()

    ap.add_argument(
        '-v',
        '--verbose',
        default=False,
        action='store_true',
        help='Increase output verbosity'
    )

    ap.add_argument('settings', help='Enigma machine settings ini file')
    ap.add_argument('message', help='Message to parse into the enigma machine')

    return ap.parse_args()
