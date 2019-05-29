import binascii
import unittest

from encoding.base58_check import Base58CheckAddress
from encoding.byte_conversion import to_n_bits
from encoding.cashaddr import AddressType, Cashaddr


class CashaddrTest(unittest.TestCase):
    def test_polymod(self):
        """
        Polymod should return 0
        """
        cashaddr = "bitcoincash:qqjsprfudecxwurfswv0sjvvt8lhxf6zqvapsewce9"
        addr = Cashaddr()
        
        payload =  addr.lower_prefix_bits() + [0] + addr.reverse_map(cashaddr.split(":")[1])

        self.assertEqual(0, addr.poly_mod(payload))

    def test_encoding(self):
        btc = Base58CheckAddress()
        bch = Cashaddr()
        ripemd = btc.decode_base58("31nwvkZwyPdgzjBJZXfDmSWsC4ZLKpYyUw")
        print("RIPEMD IS {}".format(binascii.hexlify(ripemd)))
        bch.hash = ripemd[1:-4]

        self.assertEqual("bitcoincash:pqq3728yw0y47sqn6l2na30mcw6zm78dzq5ucqzc37", bch.address_string(AddressType.P2SH))

    def test_byte_split(self):
        byte_arr = bytes([255, 255])
        five_bits = to_n_bits(byte_arr)

        self.assertSequenceEqual(five_bits, bytes([31, 31, 31, 16]))

        self.assertSequenceEqual(byte_arr, to_n_bits(five_bits, 5, 8)[:-1])
