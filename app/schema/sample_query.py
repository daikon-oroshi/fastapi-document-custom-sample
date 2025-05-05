from typing import Literal
from pydantic import BaseModel, Field, field_serializer, field_validator
from datetime import date, datetime
from typing import ClassVar
from .sample_enum import SampleEnum


class SampleQuery(BaseModel):
    """
    SampleQuery docstring here
    """

    q_str: str = Field(
        ...,
        title="q_str title here",
        description="q_str description here",
        max_length=50,
        min_length=3,
        example="aaaa",
        pattern=r"^[a-zA-Z0-9_]+$",
    )
    q_int: int = Field(
        ...,
        title="q_int title here",
        description="q_int description here",
        ge=1,
        le=100,
    )
    q_int_nullable: int | None = Field(
        10,
        title="q_int_nullable title here",
        description="q_int_nullable description here",
    )
    q_nullable_default_none: int | None = Field(
        None,
        title="q_nullable_default_none title here",
        description="q_nullable_default_none description here",
    )
    nullable: int | None = Field(
        ...,
        title="nullable title here",
        description="nullable description here",
    )
    q_list: list[str] = Field(
        ...,
        title="q_list title here",
        description="q_list description here",
        example=["aaa", "bbb"],
        max_length=2,
    )
    q_enum: SampleEnum = Field(
        ...,
        title="q_enum title here",
        description="q_enum description here",
        example=SampleEnum.BBB,
    )
    q_literal: Literal["01", "02", "03"] = Field(
        ...,
        title="q_literal title here",
        description="q_literal description here",
        example="01",
    )

    q_date: date = Field(
        ..., title="q_date title here", description="q_date description here"
    )
    q_datetime: datetime = Field(
        ...,
        title="q_datetime title here",
        description="q_datetime description here",
        example="2023/10/01 12:00:00",
        json_schema_extra={"format": "%Y/%m/%d %H:%M:%S"},
    )

    datetime_format: ClassVar[str] = "%Y/%m/%d %H:%M:%S"

    @field_validator("q_datetime", mode="before")
    def string_to_datetime(cls, v: object) -> datetime:
        if isinstance(v, str):
            return datetime.strptime(v, cls.datetime_format)
        return v

    @field_serializer("q_datetime")
    def serialize_datetime(self, q_datetime: datetime) -> str:
        return q_datetime.strftime(self.datetime_format)
