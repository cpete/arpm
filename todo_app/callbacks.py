from dash import Dash, Input, Output, State
from dash.exceptions import PreventUpdate

from todo_app.layout import render_todos
from todo_app.store import TodoStore


def register_callbacks(app: Dash, store: TodoStore) -> None:
    @app.callback(
        Output("todo-list", "children"),
        Output("new-todo", "value"),
        Input("add-todo", "n_clicks"),
        State("new-todo", "value"),
        prevent_initial_call=True,
    )
    def add_todo(_clicks: int, text: str | None):
        if not text or not text.strip():
            raise PreventUpdate
        store.add(text.strip())
        return render_todos(store.list()), ""
