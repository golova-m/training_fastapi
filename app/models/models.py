from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str


class Feedback(BaseModel):
    name: str
    message: str