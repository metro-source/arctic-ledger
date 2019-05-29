##
# Key generation happens here
import binascii

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

class Keys(object):
    """
    Base class for the others
    """
    def __init__(self, private_key = None, public_key = None):
        # These should always be an instance of the cryptography module's primitives
        self.private_key = private_key
        self.public_key = public_key
    
    def gen_key_pair(self):
        raise NotImplementedError()

    def public_key_hash(self):
        """
        Should return a string with the hex representation of the public key hash
        """
        raise NotImplementedError()

    def derive_public_key(self):
        """
        Generate the public key using the current private key
        """
        return self.private_key.public_key()

    def key_pair_valid(self):
        """
        Validate current key pair 
        """
        if self.private_key is None or self.public_key is None:
            return False 
        
        """
        TODO: Extra validation
        """
        return True

    def load_private_key_number(self, number):
        if type(number) is str:
            number = int(number, 16)
        
        self.private_key = ec.derive_private_key(number, ec.SECP256K1(), default_backend())

class BitcoinKeys(Keys):
    def gen_key_pair(self):
        self.private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        self.public_key = self.private_key.public_key()

    def public_key_hash(self):
        point = self.public_key.public_numbers().encode_point()

        return binascii.hexlify(point)

    def private_key_hash(self):
        return "%x" % self.private_key.private_numbers().private_value