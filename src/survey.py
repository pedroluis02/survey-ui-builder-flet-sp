from dataclasses import dataclass
from enum import Enum


class FieldType(Enum):
    FREE_TEXT = "FreeText"


@dataclass
class SurveyStep:
    question: str
    field_type: str = FieldType.FREE_TEXT
    description: str = ""


@dataclass
class Survey:
    name: str
    steps: list[SurveyStep]
