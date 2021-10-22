from dataclass_factory import Schema
from dataclasses import dataclass

from typing import Union


class URL:
    new_install = 'https://ashyq.curs.kz/ashyq/v2/api/otp/newInstall'
    connect = 'https://ashyq.curs.kz/ashyq/identity/connect/token'
    user = 'https://ashyq.curs.kz/ashyq/v2/api/user'
    qrpass = 'https://ashyq.curs.kz/ashyq/v2/api/qrpass/check'
    employee_check = 'https://ashyq.curs.kz/ashyq/v2/api/qrpass/employee/check'


@dataclass
class Code(Schema):
    code: None


@dataclass
class Connect(Schema):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str


@dataclass
class User(Schema):
    id: str
    entry_scanner: bool
    apartment: Union[str, None]
    building: Union[str, None]
    home_phone_number: Union[str, None]
    house: Union[str, None]
    first_name: Union[str, None]
    last_name: Union[str, None]
    email: Union[str, None]
    mobile_phone_number: Union[str, None]
    patronymic_name: Union[str, None]
    photo_url: Union[str, None]
    street: Union[str, None]


@dataclass
class Check(Schema):
    bin: str
    iin: str
    code: str
    building_rka: str
    name: str
    date: str
    indicator: str
    status: str
    status_id: int
    status_description: str
    message: str
    type: str
    _pass: bool
