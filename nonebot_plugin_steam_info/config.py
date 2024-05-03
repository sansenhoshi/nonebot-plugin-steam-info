from pydantic import BaseModel


class Config(BaseModel):
    steam_api_key: str
    proxy: str = None
    steam_request_interval: int = 300  # seconds
    steam_broadcast_type: str = "part" # all, part, none
