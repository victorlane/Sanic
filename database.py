import libsql_client
from libsql_client import Client
from typing import Optional


class Turso:
    def __init__(self, url: Optional[str], token: Optional[str]):
        if not isinstance(url, str) or not isinstance(token, str):
            raise ValueError("Turso url or token is not valid.")

        self.url = url
        self.token = token

    async def get_client(self) -> Client:
        return libsql_client.create_client(self.url, auth_token=self.token)
