import flet as ft

from src.survey import Survey, SurveyStep
from src.survey_view import SurveyView


def main(page: ft.Page):
    survey = Survey(
        name="Survey 1",
        steps=[
            SurveyStep(question="What is your name?"),
            SurveyStep(question="What is your lastname?"),
            SurveyStep(question="What is your lastname?")
        ]
    )

    page.add(
        ft.SafeArea(
            SurveyView(survey),
            expand=True,
        )
    )


ft.app(main)
