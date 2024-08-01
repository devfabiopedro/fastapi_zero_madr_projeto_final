from pydantic import BaseModel


class MessageSchema(BaseModel):
    message: str


class ErrorDetail(BaseModel):
    detail: str
