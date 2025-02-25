from src.duskcore.security.key_store import KeyStore
from src.duskcore.models.keychain import KeyChainModel
from Crypto.Random import get_random_bytes

def test_keyDecryptsData():
    key = get_random_bytes(32)
    salt = get_random_bytes(32)
    chain = KeyChainModel(
        passkey=key,
        salt=salt
    )
    store = KeyStore()
    store.set_chain(chain)
    raw_data = "asdf"
    encrypted_data = store.encrypt(raw_data)
    decrypted_data = store.decrypt(encrypted_data)
    assert decrypted_data == raw_data

def test_keyDecryptsDuringKeyRotation():
    key_1 = get_random_bytes(32)
    salt_1 = get_random_bytes(32)
    key_2 = get_random_bytes(32)
    salt_2 = get_random_bytes(32)
    chain_1 = KeyChainModel(
        passkey=key_1,
        salt=salt_1
    )
    chain_2 = KeyChainModel(
        passkey=key_2,
        salt=salt_2
    )
    store = KeyStore()
    store.set_chain(chain_1)
    raw_data = "asdf"
    encrypted_data = store.encrypt(raw_data)
    store.set_chain(chain_2)
    decrypted_data = store.decrypt(encrypted_data)
    assert decrypted_data == raw_data