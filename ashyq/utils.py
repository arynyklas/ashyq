from . import types

from string import ascii_uppercase, ascii_lowercase, digits
from random import choice

from dataclass_factory import Factory, Schema, NameStyle


_chars = ascii_uppercase + ascii_lowercase + digits


factory = Factory(default_schema=Schema(
    name_style=NameStyle.camel
), schemas={
    types.Code: Schema(
        name_style=NameStyle.snake
    ),
    types.Connect: Schema(
        name_style=NameStyle.snake
    ),
    types.Check: Schema(
        name_mapping={
            'bin': 'BIN',
            'building_rka': 'BuildingRKA',
            'iin': 'IIN',
            '_pass': 'Pass'
        }
    )
})


def random_string(length: int) -> str:
    return ''.join(choice(_chars) for _ in range(length))


def to_object(data: dict, data_class: Schema, snake: bool=False) -> Schema:
    return factory.load(data, data_class)
