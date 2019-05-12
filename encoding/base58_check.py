from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import binascii

class Base58CheckAddress(object):
    ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    VERSION_BYTE = bytes([0])
    
    def __init__(self, public_key = None):
        """
        Where public key is an instance of ec.EllipticCurvePublicKey
        """
        self.payload_bin = None
        self.payload_str = None

        if public_key:
            self.load_public_key(load_public_key)

        self.ripemd_hash = None
    
    def load_public_key(self, public_key)
        self.payload_bin = public_key.public_numbers().encode_point()
        self.payload_str = binascii.hexlify(self.payload_bin)


    def set_ripemd(self):
        self.ripemd_hash = self.hash_ripemd(self.payload_bin)
    
    def hash_ripemd(self, payload: bytes):
        sha256 = self.hash_sha256(payload)

        ripemd = hashes.Hash(hashes.RIPEMD160(), backend=default_backend())
        ripemd.update(sha256)

        return ripemd.finalize()

    def hash_sha256(self, payload: bytes):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(payload)

        return digest.finalize()

    def address_string(self):
        self.set_ripemd()
        assert self.ripemd_hash != None, "RIPEMD160 Hash is None"

        extended = self.VERSION_BYTE + self.ripemd_hash
        first_hash = self.hash_sha256(extended)
        payload_hashed = self.hash_sha256(first_hash)

        checksum = payload_hashed[:4]

        concatenated = extended + checksum

        return self.encode_base58(concatenated)

    def encode_base58(self, payload: bytes):
        bignum = int.from_bytes(payload, byteorder='big', signed=False)
        address = ""

        while bignum:
            remainder = bignum % 58
            bignum //= 58
            address += self.ALPHABET[remainder]
        
        zero_byte = bytes(1)[0]
        for byte in payload:
            if byte != zero_byte:
                break
            address += self.ALPHABET[0]

        return address[::-1]

