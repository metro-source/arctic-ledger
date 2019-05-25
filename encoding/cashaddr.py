"""
Cashaddr implementation
Based on https://github.com/bitcoincashorg/bitcoincash.org/blob/master/spec/cashaddr.md
"""
from enum import Enum
from encoding.byte_conversion import to_n_bits

class AddressType(Enum):
    P2KH = 0
    P2SH = 1

class InvalidHashSize(Exception):
    pass

class Cashaddr(object):
    def __init__(self):
        self.ALPHABET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
        self.map = { c: i for i,c in enumerate(self.ALPHABET)}
        self.prefix = "bitcoincash"
        self.separator = ":"

        """
        The payload is composed of 3 elements:

            A version byte indicating the type of address.
            A hash.
            A 40 bits checksum.
        """
        self.payload = None

        """
        The hash representing the data
        """
        self.hash = None

    def lower_prefix_bits(self):
        """
        Returns the lower 5 bits of each char in the prefix
        """
        return [ord(c) & 0b11111 for c in self.prefix]

    def hash_size_bits(self):
        return len(self.hash) * 8

    def get_size_bits(self):
        size_map = {
            160: 0,
            192: 1,
            224: 2,
            256: 3,
            320: 4,
            384: 5,
            448: 6,
            512: 7
        }
        hash_bits  = self.hash_size_bits()
        print("Address size is {}".format(hash_bits))
        if hash_bits not in size_map:
            raise InvalidHashSize("Invalid hash size of {} bits".format(hash_bits))
        
        return size_map[hash_bits]

    def reverse_map(self, payload_str):
        """
        Map each char to their base32 index
        """
        return [ self.map[char] for char in payload_str ]

    def get_version_byte(self, address_type):
        version_byte = 0

        if address_type == AddressType.P2SH:
            version_byte = 8
        
        version_byte += self.get_size_bits()

        return version_byte

    def address_string(self, address_type):
        prefix = [
            *self.lower_prefix_bits(),
            0
        ]

        payload = to_n_bits(bytes([self.get_version_byte(address_type)]) + self.hash)

        checksum = self.poly_mod(prefix + list(payload) + [0]*8)
        checksum_bytes = bytes((checksum >> (5 * (7 - i))) & 31 for i in range(8))

        return self.prefix + self.separator + self.encode_base32(payload + checksum_bytes)

    def encode_base32(self, vector):
        return ''.join([ self.ALPHABET[c] for c in vector ])

    def poly_mod(self, vector):
        c = 1

        for d in vector:
            c0 = c >> 35
            c = ((c & 0x07ffffffff) << 5) ^ d

            if (c0 & 1):
                c ^= 0x98f2bc8e61
            if (c0 & 2):
                c ^= 0x79b76d99e2
            if (c0 & 4):
                c ^= 0xf33e5fb3c4
            if (c0 & 8):
                c ^= 0xae2eabe2a8
            if (c0 & 16):
                c ^= 0x1e4f43e470

        return c ^ 1

