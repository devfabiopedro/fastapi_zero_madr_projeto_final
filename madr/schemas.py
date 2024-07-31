from pydantic import BaseModel, EmailStr

"""___________________________________________________________________ Message
"""


class MessageSchema(BaseModel):
    message: str


"""___________________________________________________________________ Account
"""


class AccountSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


"""_____________________________________________________________________ Books
"""


class BookSchema(BaseModel):
    year: int
    title: str
    novelist_id: int


"""_________________________________________________________________ Novelists
"""


class NovelistSchema(BaseModel):
    name: str
