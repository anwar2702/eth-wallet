#!/usr/bin/env python3

from eth_wallet.wallet import Wallet

import pytest


MNEMONIC = "indicate warm sock mistake code spot acid ribbon sing over taxi toast"
PASSPHRASE = None
LANGUAGE = "english"


def test_from_mnemonic():

    wallet = Wallet()
    wallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)

    wallet.from_index(44, harden=True)
    wallet.from_index(60, harden=True)
    wallet.from_index(0, harden=True)
    wallet.from_index(0)
    wallet.from_index(0, harden=True)

    assert wallet.entropy() is None
    assert wallet.mnemonic() == \
        "indicate warm sock mistake code spot acid ribbon sing over taxi toast"
    assert wallet.language() == "english"
    assert wallet.passphrase() is None
    assert wallet.seed() == "baff3e1fe60e1f2a2d840d304acc98d1818140c79354a353b400fb019bfb256bc392d7aa9047adff1f14b" \
                            "ce0342e14605c6743a6c08e02150588375eb2eb7d49"
    assert wallet.private_key() == "678d12447649cc9eeede87562069c2ff1524f31df025f521be255d4a6c8eaed0"
    assert wallet.public_key() == "03df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f"
    assert wallet.uncompressed() == "df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f1e4f78a8cae1d" \
                                    "af5dd1a716a96475b16dcfb455e7d97fe75dd8f1f8ea5cc0a41"
    assert wallet.compressed() == "03df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f"
    assert wallet.wallet_import_format() == "KzgzzJkyzqcy8bLJDPLwXV5VmJER3f35q9zyAgSdMLn6aqMovQ66"
    assert wallet.finger_print() == "2004e94c"
    assert wallet.chain_code() == "67a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93def287754"
    assert wallet.path() == "m/44'/60'/0'/0/0'"
    assert wallet.address() == "0xAaB4E88BCa0d7C1e40CE540b9642558d6f9a3a05"

    assert wallet.extended_key(private_key=True, encoded=False) == "0488ade405f450d7af8000000067a537696eecbfdd5755" \
                                                                   "734eee16dca622e62bb3c98f66db89cad93def28775400" \
                                                                   "678d12447649cc9eeede87562069c2ff1524f31df025f5" \
                                                                   "21be255d4a6c8eaed0"
    assert wallet.extended_key(private_key=False, encoded=False) == "0488b21e05f450d7af8000000067a537696eecbfdd575" \
                                                                    "5734eee16dca622e62bb3c98f66db89cad93def287754" \
                                                                    "03df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8" \
                                                                    "074fc2415d78ed1a3e73f"
    assert wallet.extended_key(private_key=True, encoded=True) == "xprvA4Dqp8w5LcQejoog9rci7sadBJetitNj1wvbG7uHLLk" \
                                                                  "SxoFhkzVnZ7A8Z6Kz4VRMpFSJ2Kct9KFf8uVpuWiqU9vBrk" \
                                                                  "h9w6dVfThmF4RUxHV"
    assert wallet.extended_key(private_key=False, encoded=True) == "xpub6HDCDeTyAyxwxHt9Ft9iV1XMjLVP8M6aPArC4WJttg" \
                                                                   "HRqbarJXp36uUcQQDJwBK3GEhKy7cbV1Fs4UoRDRpbhTFR" \
                                                                   "ZmPJ3coUuenN2TARncR"

    assert wallet.dumps() == {
        "entropy": None,
        "mnemonic": "indicate warm sock mistake code spot acid ribbon sing over taxi toast",
        "language": "english",
        "passphrase": None,
        "seed": "baff3e1fe60e1f2a2d840d304acc98d1818140c79354a353b400fb019bfb256bc392d7aa9047adff1f14bce0342e14605c6743a6c08e02150588375eb2eb7d49",
        "root_private_key": "f7239ecece685b42e768a3b3d5f8f67946e6f8e5f008a46fb80d34a69977be9a93d3aaf6c13639763807811805101ccab1ef09774e71afa028847dadfb0232e0",
        "root_public_key": "222d5011dfc66eabaa4d994ee66754a54eac0cf2633e4c9920abb7ba94ab4b7cb18aed261ccdd9d50e2bd2ca6a776d826201e1b1b0d953fae75f4da1167337e7",
        "uncompressed": "df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f1e4f78a8cae1daf5dd1a716a96475b16dcfb455e7d97fe75dd8f1f8ea5cc0a41",
        "compressed": "03df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f",
        "chain_code": "67a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93def287754",
        "private_key": "678d12447649cc9eeede87562069c2ff1524f31df025f521be255d4a6c8eaed0",
        "public_key": "03df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f",
        "wif": "KzgzzJkyzqcy8bLJDPLwXV5VmJER3f35q9zyAgSdMLn6aqMovQ66",
        "finger_print": "2004e94c",
        "path": "m/44'/60'/0'/0/0'",
        "address": "0xAaB4E88BCa0d7C1e40CE540b9642558d6f9a3a05",
        "serialized": {
            "private_key_hex": "0488ade405f450d7af8000000067a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93def28775400678d12447649cc9eeede87562069c2ff1524f31df025f521be255d4a6c8eaed0",
            "public_key_hex": "0488b21e05f450d7af8000000067a537696eecbfdd5755734eee16dca622e62bb3c98f66db89cad93def28775403df79315f83cfeaadbd88bfc0033367ebd2ca7e08df8074fc2415d78ed1a3e73f",
            "private_key_base58": "xprvA4Dqp8w5LcQejoog9rci7sadBJetitNj1wvbG7uHLLkSxoFhkzVnZ7A8Z6Kz4VRMpFSJ2Kct9KFf8uVpuWiqU9vBrkh9w6dVfThmF4RUxHV",
            "public_key_base58": "xpub6HDCDeTyAyxwxHt9Ft9iV1XMjLVP8M6aPArC4WJttgHRqbarJXp36uUcQQDJwBK3GEhKy7cbV1Fs4UoRDRpbhTFRZmPJ3coUuenN2TARncR"
        }
    }

    with pytest.raises(ValueError, match=r".*12 word mnemonic.*"):
        wallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language="chinese_traditional")

    assert wallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=None)

    with pytest.raises(ValueError, match=r"Invalid language, .*"):
        wallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language="amharic")
