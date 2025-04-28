import flet as ft

from src.survey import Survey, SurveyStep


class SurveyView(ft.Container):
    survey: Survey
    step_index: int = 0
    step: SurveyStep

    step_question_view: ft.Text
    step_field_view: ft.TextField

    def __init__(self, survey: Survey):
        self.survey = survey
        self.step = self.survey.steps[self.step_index]

        self.step_question_view = ft.Text(self.step.question)
        self.step_field_view = ft.TextField("")

        super().__init__(
            ft.Column(
                controls=[
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
                        ],

                    ),
                    ft.Row(
                        controls=[
                            ft.FloatingActionButton(icon=ft.Icons.ARROW_LEFT, on_click=self.previous_click),
                            ft.FloatingActionButton(icon=ft.Icons.ARROW_RIGHT, on_click=self.next_click),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                ],
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.all(20)
        )

    def previous_click(self, _):
        if self.step_index > 0:
            self.step_index = self.step_index - 1
            self.step = self.survey.steps[self.step_index]

            self.step_question_view.value = self.step.question
            self.step_question_view.update()

    def next_click(self, _):
        if self.step_index < len(self.survey.steps) - 1:
            self.step_index = self.step_index + 1
            self.step = self.survey.steps[self.step_index]

            self.step_question_view.value = self.step.question
            self.step_question_view.update()
