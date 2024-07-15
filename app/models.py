from dataclasses import dataclass
from datetime import datetime
from typing import List
from bson import ObjectId


@dataclass
class User:
    _id: str
    number: int
    devision: str
    email: str
    password: str
    
@dataclass
class Stock:
    _id: str
    is_in_coming: bool
    title: str
    description: str
    date: datetime
    quantity: int
    quantity_type: str
    serial_number: str
    devision: str
    sender: str
    receivery: str
    remark: str
    images: List[str]