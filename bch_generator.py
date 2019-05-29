"""
Generates BCH Wallets
"""
from keys import BitcoinKeys
from encoding.base58_check import Base58CheckAddress
from encoding.cashaddr import Cashaddr, AddressType

print("Generating a new keypair")

my_keys = BitcoinKeys()
my_keys.gen_key_pair()

legacy =  Cashaddr(my_keys.public_key)

print("Private key: {}".format(my_keys.private_key_hash()))
print("Public key: {}".format(my_keys.public_key_hash()))
print("Address: {}".format(legacy.address_string(AddressType.P2KH)))