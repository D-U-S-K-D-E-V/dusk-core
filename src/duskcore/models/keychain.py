from src.duskcore.security.key import Key
from dataclasses import dataclass

@dataclass
class KeyChainModel():
    passkey: Key
    salt: Key