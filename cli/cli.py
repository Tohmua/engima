from argparse import ArgumentParser
from cli.settings import Settings
from machine.factory import create as machineFactory


def main():
    args = getCliArguments()
    settings = Settings(args.settings)
    machine = machineFactory(settings)

    output = []

    for letter in list(args.message):
        output.append(machine.encode(letter))

    print(''.join(output))


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
