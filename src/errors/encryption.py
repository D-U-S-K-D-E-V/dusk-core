class InvalidEncryptionKeyError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidKeyError(Exception):
    def __init__(self, message):
        super().__init__(message)