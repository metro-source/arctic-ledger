# Just test everything
import unittest
import keys

class KeyTest(unittest.TestCase):
    def test_bitcoin(self):
        btc = keys.BitcoinKeys()
        btc.gen_key_pair()

        self.assertTrue(btc.private_key is not None)
        self.assertTrue(btc.public_key is not None)
        self.assertTrue(btc.key_pair_valid())