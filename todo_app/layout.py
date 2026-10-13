from dash import html


def build_layout() -> html.Div:
    return html.Div(
        [
            html.H1("Todo List"),
            # TODO: input for new todos
            # TODO: list of todos
        ],
        id="app-root",
    )
