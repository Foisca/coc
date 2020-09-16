from Crypto.Util.number import *  # noqa: F403

__revision__ = ...  # type: str

class pubkey:
    def __init__(self) -> None: ...
    def encrypt(self, plaintext, K): ...
    def decrypt(self, ciphertext): ...
    def sign(self, M, K): ...
    def verify(self, M, signature): ...
    def validate(self, M, signature): ...
    def blind(self, M, B): ...
    def unblind(self, M, B): ...
    def can_sign(self): ...
    def can_encrypt(self): ...
    def can_blind(self): ...
    def size(self): ...
    def has_private(self): ...
    def publickey(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
