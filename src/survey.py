from dataclasses import dataclass


@dataclass
class SurveyStep:
    question: str
    field_type: str
    description: str = ""


@dataclass
class Survey:
    name: str
    steps: list[SurveyStep]
