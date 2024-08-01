from pydantic import BaseModel


class NovelistSchema(BaseModel):
    name: str
