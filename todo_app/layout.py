from dash import dcc, html

from todo_app.store import Todo


def render_todos(todos: list[Todo]) -> list[html.Li]:
    return [
        html.Li(
            [
                html.Span(todo.text),
                html.Button(
                    "Delete",
                    id={"type": "delete-todo", "index": todo.id},
                    n_clicks=0,
                ),
            ]
        )
        for todo in todos
    ]


def build_layout(todos: list[Todo] | None = None) -> html.Div:
    return html.Div(
        [
            html.H1("Todo List"),
            dcc.Input(id="new-todo", type="text",
                      placeholder="New todo", debounce=True),
            html.Button("Add", id="add-todo", n_clicks=0),
            html.Ul(render_todos(todos or []), id="todo-list"),
        ],
        id="app-root",
    )
