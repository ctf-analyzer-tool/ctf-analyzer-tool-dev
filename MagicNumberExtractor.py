import binascii
from argparse import ArgumentParser

parser = ArgumentParser()
filename = parser.add_argument("-f", dest="filename", help="Path of file")
args = parser.parse_args()
with open(args.filename, "rb") as binary_file:
    data = binary_file.read()
    data = data[0:4]
    data = binascii.hexlify(data)
    data = data.decode('utf-8')
    print('[+] Magic number of the given file: ', data)
