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

        self.assertIsNotNone(addr)
        self.assertIsInstance(addr, str)
        self.assertEqual("16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM", addr)
