from pydantic_core import core_schema as cs
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from enum import Enum


class CustomSchemaEnum(Enum):
    @classmethod
    def get_names(cls):
        return [e.name for e in cls]

    @classmethod
    def get_values(cls):
        return [e.value for e in cls]

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: cs.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        json_schema = handler(core_schema)
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema["x-enum-varnames"] = cls.get_names()
        return json_schema


class SampleEnum(str, CustomSchemaEnum):
    """
    SampleEnum docstring here
    """

    AAA = "01"
    BBB = "02"
    CCC = "03"


class PrefCode(str, CustomSchemaEnum):
    HOKKAIDO = "01"
    AOMORI = "02"
    IWATE = "03"
    MIYAGI = "04"
    AKITA = "05"
    YAMAGATA = "06"
    FUKUSHIMA = "07"
    IBARAKI = "08"
    TOCHIGI = "09"
    GUNMA = "10"
    SAITAMA = "11"
    CHIBA = "12"
    TOKYO = "13"
    KANAGAWA = "14"
    # ...以下省略...
