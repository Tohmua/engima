from plugboard.plugboard import PlugBoard
from rotor.rotor_i import RotorI
from reflector.reflector_a import ReflectorA
from enigma.enigma import Enigma


plugboard = PlugBoard({'a': 'b', 'c': 'd', 'e': 'f'})
rotor1 = RotorI()
rotor2 = RotorI()
rotor3 = RotorI()
reflector = ReflectorA()

enigma = Enigma(plugboard, [rotor1, rotor2, rotor3], reflector)

stringToBeEncoded = str(input("Message To Encrypt: "))

output = []

for letter in list(stringToBeEncoded):
    output.append(enigma.encode(letter))

print(''.join(output))
