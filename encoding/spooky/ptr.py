from encoding.base58_check import Base58CheckAddress

"""
You don't wanna know.
"""
class Ptr(Base58CheckAddress):
    VERSION_BYTE = bytes([117])