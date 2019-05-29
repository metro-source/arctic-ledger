# Arctic Ledger

A set of tools for working with cryptocurrencies in Python

**Supported cryptos:**
- Bitcoin (Basic, no segwit or P2SH support yet)
- Bitcoin Cash (Same as btc, no p2sh yet)

**Planned to be included:**
- IOTA
- Monero

## Features
---
- Key generation for BTC & BCH
- Encoding & decoding of addresses

## Future Features
---
    - HD Wallet support

## Examples

### Generating a bitcoin wallet

```python
"""
Generates BTC Wallets
"""
from keys import BitcoinKeys
from encoding.base58_check import Base58CheckAddress

print("Generating a new keypair")

my_keys = BitcoinKeys()
my_keys.gen_key_pair()

btc =  Base58CheckAddress(my_keys.public_key)

print("Private key: {}".format(my_keys.private_key_hash()))
print("Public key: {}".format(my_keys.public_key_hash()))
print("Address: {}".format(btc.address_string()))
```

### Generating a Bitcoin Cash wallet

```python
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
```

## Motivations behind this project
---
- Research & learning
- Create a library for apps to collect payments programatically

## License
---
The MIT license. See the license file included in this project for more information.