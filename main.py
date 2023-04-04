import rlp
from eth_typing import HexStr
from eth_utils import to_bytes
from ethereum.transactions import Transaction
from pprint import pprint


def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


if __name__ == '__main__':
    tx_raw = str(input('Enter raw transaction: '))
    tx = rlp.decode(hex_to_bytes(tx_raw), Transaction)
    pprint(tx.to_dict())
