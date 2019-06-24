import binascii
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f","--file", metavar="filename", type=str, nargs=1, help="Path of the file")
args = parser.parse_args()

with open(args.file[0], "rb") as binary_file:
    data = binary_file.read()
    data = data[0:4]
    data = binascii.hexlify(data)
    data = data.decode('utf-8')
    print('[+] Magic number of the given file: ', data)
