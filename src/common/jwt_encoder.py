from injector import inject
from jose import jwt

from src.common.i_jwt_encoder import IJwtEncoder
from src.common.settings import Settings


class JwtEncoder(IJwtEncoder):
    @inject
    def __init__(self, settings: Settings):
        self.__secret = settings.authentication_secret
        self.__algorithm = "HS256"

    def encode(self, data: dict) -> str:
        return jwt.encode(data, self.__secret, algorithm=self.__algorithm)

    def decode(self, encoded_data: str) -> dict:
        return jwt.decode(encoded_data, self.__secret, algorithms=[self.__algorithm])
