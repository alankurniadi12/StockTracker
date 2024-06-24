from dataclasses import dataclass, field
from datetime import datetime


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
    title: str
    description: str
    date: datetime
    quantity: int
    quantity_type: str
    serial_number: str
    to_devision: str
    send_by: str
    received_by: str
    remark: str


