import datetime
from db import database, metadata
from typing import Optional
import ormar


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(MainMeta):
        tablename = "user"

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100)


class Video(ormar.Model):
    class Meta(MainMeta):
        tablename = "video"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=100)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user_id: Optional[User] = ormar.ForeignKey(User)

