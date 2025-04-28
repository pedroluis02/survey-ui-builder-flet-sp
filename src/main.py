import flet as ft

from src.survey import Survey, SurveyStep


def main(page: ft.Page):
    survey = Survey(
        name="Survey 1",
        steps=[
            SurveyStep(question="What is your name?"),
            SurveyStep(question="What is your lastname?")
        ]
    )
    survey_step_index = 0
    survey_step = survey.steps[survey_step_index]

    survey_step_text = ft.Text(survey_step.question)
    survey_step_field = ft.TextField(value="")

    def next_step_click(_):
        nonlocal survey_step_index
        nonlocal survey_step

        if survey_step_index < len(survey.steps) - 1:
            survey_step_index = survey_step_index + 1
            survey_step = survey.steps[survey_step_index]

            survey_step_text.value = survey_step.question
            survey_step_text.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ARROW_RIGHT, on_click=next_step_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column(
                    controls=[
                        ft.Text(survey.name),
                        ft.VerticalDivider(width=12),
                        ft.Column(
                            controls=[
                                survey_step_text,
                                survey_step_field
                            ]
                        )
                    ]
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.all(20)
            ),
            expand=True,
        )
    )


ft.app(main)
