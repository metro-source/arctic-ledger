def to_n_bits(input, input_bits = 8, output_bits = 5):
    """
    Convert an array of N-bits integer into an array of N'-bits integers
    """
    carry = 0
    bits_count = 0
    output = []

    for number in input:
        carry = carry << input_bits
        carry += number
        bits_count += input_bits

        while bits_count >= output_bits:
            number = (carry >> (bits_count - output_bits))
            output.append(number)
            carry -= (number << bits_count - output_bits)
            bits_count -= output_bits

    if bits_count and output_bits > bits_count:
        output.append(carry << (output_bits - bits_count))
        
    return bytes(output)

def _convertbits(data, frombits, tobits, pad=True):
    """General power-of-2 base conversion."""
    acc = 0
    bits = 0
    ret = bytearray()
    maxv = (1 << tobits) - 1
    max_acc = (1 << (frombits + tobits - 1)) - 1
    for value in data:
        acc = ((acc << frombits) | value) & max_acc
        bits += frombits
        while bits >= tobits:
            bits -= tobits
            ret.append((acc >> bits) & maxv)

    if pad and bits:
        ret.append((acc << (tobits - bits)) & maxv)

    return ret