import datetime
from enum import Enum

from pydantic import BaseModel, field_validator


class Level(Enum):
    BEGINER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    date_joined: datetime.date
    level: Level

    @field_validator("age")
    def validate_age(cls, age):
        if age < 10:
            raise ValueError("Age must be 10 or above")
        return age

    @field_validator("level")
    def validate_level_from_age(cls, level, values):
        print(level)
        return level


student = Student(
    first_name="Harry",
    last_name="Potter",
    age=19,
    date_joined=datetime.date(2020, 1, 1),
    level=Level.ADVANCED,
)

print(student)
