from pydantic import BaseModel

class EncryptedPayloadModel(BaseModel):
    ciphertext: str
    tag: str
    nonce: str
