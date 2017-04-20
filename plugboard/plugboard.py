class PlugBoard(object):

    board = {
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

    def __init__(self, positions: dict = {}):
        if self.validate(positions):
            self.board = self.buildBoard(self.board, positions)

    def validate(self, positions: dict) -> bool:
        usedPairs = {}

        for k, v in positions.items():
            if k in usedPairs.keys() or v in usedPairs.keys():
                raise Exception('Unable to set {} <-> {}'.format(k, v))

            usedPairs.update({k: v})

        return True

    def buildBoard(self, board: dict, positions: dict) -> dict:
        for k, v in positions.items():
            if k in board.keys() and v in board.keys():
                board.update({k: v})
                board.update({v: k})

        return board

    def parse(self, key: str) -> str:
        return self.board.get(key)
