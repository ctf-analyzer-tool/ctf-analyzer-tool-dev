import binascii
from argparse import ArgumentParser
import json
import msgpack 

print('')
parser = ArgumentParser()
filename = parser.add_argument("-f", dest="filename", help="Path of file")
args = parser.parse_args()
with open(args.filename, "rb") as binary_file:
    data = binary_file.read()
    data = binascii.hexlify(data[0:4]).decode('utf-8').upper()
    data = ' '.join([data[i:i+2] for i in range(0, len(data), 2)])
    print('[+] Magic number of the given file =', data)

with open('/home/nullvoiddeath/PycharmProjects/ctf-analyzer-tool/MagicNumberDB.json', 'r') as f:
    MagicNumbers = json.load(f)

for Hash in MagicNumbers:
    i = 0
    if data == Hash['Signature']:
        print('[+] File type is =', Hash['Type'])
        print('[+] Tools to use ↴')
        for Tools in Hash['Tools']:
            print('\t\t[' + str(i+1) + '] ' + Tools)
            i += 1
