# Just test everything
import unittest
import keys
import binascii
from encoding.base58_check import Base58CheckAddress

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

class AddressTest(unittest.TestCase):
    def test_bitcoin(self):
        btc = keys.BitcoinKeys()
        btc.load_private_key_number("18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725")
        btc.public_key = btc.derive_public_key()

        addr = Base58CheckAddress(btc.public_key).address_string()

        self.assertEqual("16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM", addr)

    def test_decode(self):
        addresses = [
            ('16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM', b'00010966776006953d5567439e5e39f86a0d273beed61967f6'),
            ("16w1D5WRVKJuZUsSRzdLp9w3YGcgoxDXb", b'00011F28E473C95F4013D7D53EC5FBC3B42DF8ED1004667AB6'),
            ("1L6x5HbJ1E2y8S7gZucj5ZUQpDi6UDxWjb", b'00D18A716D5FD0636EA71846D5E9F87669638161D7F4AF7DB2'),
            ("34XzC9DxtZ9aKwwASj9SNo94koLrtPLQ7a", b'051F33304D954D41ACF47884D17D3067AC90F09901D15320B1'),
            ('31nwvkZwyPdgzjBJZXfDmSWsC4ZLKpYyUw', b'05011F28E473C95F4013D7D53EC5FBC3B42DF8ED10C1B9A3FC')
        ]

        for addr, addr_bin in addresses:
            self.bitcoin_decode(addr, addr_bin)

    def bitcoin_decode(self, addr, addr_bin):
        btc = Base58CheckAddress()

        self.assertEqual(btc.decode_base58(addr), binascii.unhexlify(addr_bin))