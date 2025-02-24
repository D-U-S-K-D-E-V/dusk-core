from src.duskcore.enums.key_type import KeyTypeEnum
from src.duskcore.errors.encryption import InvalidKeyError
from typing import Union
import ctypes

class Key():
    def __init__(self, key_type: KeyTypeEnum):
        self.__key = None
        self.key_type = key_type

    def get_key(self, mutable=False) -> Union[bytes, bytearray]:
        if self.__key is None:
            raise InvalidKeyError(message="Encryption Key cannot be NoneType")
        if mutable:
            return bytearray(self.__key)
        else:
            return self.__key
        
    def set_key(self, new_key: bytes) -> None:
        if type(new_key) != bytes:
            raise InvalidKeyError(message="Encryption key must be of type bytes.")
        if len(new_key) != 32:
            raise InvalidKeyError(message="Key must be 32 bytes.")
        self.__key = new_key

    @staticmethod
    def __zero_memory(secret: bytes) -> None:
        length = len(secret)
        ctypes.memset(ctypes.addressof(ctypes.create_string_buffer(secret, length)), 0, length)