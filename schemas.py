from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str


class UploadVideo(BaseModel):
    name: str
    description: str


class GetVideo(BaseModel):
    user: User
    video: UploadVideo


class Message(BaseModel):
    message: str
