from pydantic import BaseModel, EmailStr

"""___________________________________________________________________ Message
"""


class MessageSchema(BaseModel):
    message: str


class ErrorDetail(BaseModel):
    detail: str


"""___________________________________________________________________ Account
"""


class AccountSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class AccountPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr


class AccountListSchema(BaseModel):
    accounts: list[AccountPublicSchema]
    total: int


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
