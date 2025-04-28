import flet as ft

from src.survey import Survey


class SurveyView(ft.Container):

    def __init__(self, survey: Survey):
        self.survey = survey
        self.step_index = 0
        self.step = self.survey.steps[self.step_index]

        self.step_question_view = ft.Text(self.step.question)
        self.step_field_view = ft.TextField("")

        super().__init__(
            ft.Column(
                controls=[
                    ft.Text(self.survey.name),
                    ft.VerticalDivider(width=12),
                    ft.Column(
                        controls=[
                            self.step_question_view,
                            self.step_field_view
                        ]
                    )
                ]
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.all(20)
        )
