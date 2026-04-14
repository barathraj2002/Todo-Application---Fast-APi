from typing import Any, Self

from pydantic import BaseModel, Field, field_validator


class Todolist(BaseModel):
    task : str = Field( min_length = 3 , max_length = 100 )

    @field_validator('task')
    def validate(cls, value: str):
        temp_str = value.strip()
        if len(temp_str) >= 3:
            return temp_str
        else:
            raise ValueError("Must be a valid value")


class response(BaseModel):
    id : int
    task : str


