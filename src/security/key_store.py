import threading
from src.models.keychain import KeyChainModel
from src.models.encrypted_payload import EncryptedPayloadModel
from src.errors.encryption import InvalidEncryptionKeyError
import ctypes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

class KeyStore:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.__previous_chain: KeyChainModel = None
        self.__current_chain: KeyChainModel = None
    
    def __get_current_chain(self) -> KeyChainModel:
        if self.__current_chain is None:
            raise InvalidEncryptionKeyError(message="Encryption Key cannot be NoneType")
        with self._lock:
            return self.__current_chain
        
    def __get_previous_chain(self) -> KeyChainModel:
        if self.__previous_chain is None:
            raise InvalidEncryptionKeyError(message="Previous Encryption Key cannot be NoneType")
        with self._lock:
            return self.__previous_chain
        
    def set_chain(self, key_chain: KeyChainModel) -> None:
        try:
            self.__previous_chain = self.__current_chain
            self.__current_chain = key_chain

        except Exception as e:
            print(e)

    def encrypt(self, data: str) -> EncryptedPayloadModel:
        keys = self.__get_current_chain()

        if self.__current_chain is None:
            raise InvalidEncryptionKeyError(message="Chain must be set before store can encrypt.")
        else:
            try:
                key = PBKDF2(keys.passkey, keys.salt, dkLen=32, count=1000000)
                cipher = AES.new(key, AES.MODE_OCB)
                ciphertext, tag = cipher.encrypt_and_digest(data.encode())
                payload = EncryptedPayloadModel(
                    ciphertext=ciphertext.hex(),
                    nonce=cipher.nonce.hex(),
                    tag=tag.hex()
                )
                return payload
            
            except Exception as e:
                raise InvalidEncryptionKeyError(message=f"error occured decrypting provided data: {e}")

    def decrypt(self, data: EncryptedPayloadModel) -> str:
        try:
            return self.__restore_data(self.__get_current_chain(), data)
        except ValueError:
            return self.__restore_data(self.__get_previous_chain(), data)

    def __restore_data(self, keys: KeyChainModel, data: EncryptedPayloadModel):
        key = PBKDF2(keys.passkey, keys.salt, dkLen=32, count=1000000)
        cipher_dec = AES.new(key, AES.MODE_OCB, nonce=bytes.fromhex(data.nonce))
        decrypted = cipher_dec.decrypt_and_verify(bytes.fromhex(data.ciphertext), bytes.fromhex(data.tag))
        return decrypted.decode()
    
    @staticmethod
    def zero_memory(secret: bytes) -> None:
        length = len(secret)
        ctypes.memset(ctypes.addressof(ctypes.create_string_buffer(secret, length)), 0, length)

            