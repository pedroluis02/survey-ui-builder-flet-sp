import flet as ft

from src.survey import Survey, SurveyStep
from src.survey_view import SurveyView


def main(page: ft.Page):
    survey = Survey(
        name="Survey 1",
        steps=[
            SurveyStep(id=1, question="What is your name?"),
            SurveyStep(id=2, question="What is your lastname?"),
            SurveyStep(id=3, question="What is your hometown?")
        ]
    )

    page.add(
        ft.SafeArea(
            SurveyView(survey),
            expand=True,
        )
    )


ft.app(main)
