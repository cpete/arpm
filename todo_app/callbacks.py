from dash import ALL, Dash, Input, Output, State, ctx
from dash.exceptions import PreventUpdate

from todo_app.layout import render_todos
from todo_app.store import TodoStore


def register_callbacks(app: Dash, store: TodoStore) -> None:
    @app.callback(
        Output("todo-list", "children"),
        Output("new-todo", "value"),
        Input("add-todo", "n_clicks"),
        Input({"type": "delete-todo", "index": ALL}, "n_clicks"),
        State("new-todo", "value"),
        prevent_initial_call=True,
    )
    def update_todos(_add_clicks: int, delete_clicks: list[int], text: str | None):
        trigger = ctx.triggered_id
        if trigger == "add-todo":
            if not text or not text.strip():
                raise PreventUpdate
            store.add(text.strip())
            return render_todos(store.list()), ""
        # Newly rendered delete buttons also fire this callback with 0 clicks.
        if isinstance(trigger, dict) and ctx.triggered[0]["value"]:
            store.remove(trigger["index"])
            return render_todos(store.list()), text
        raise PreventUpdate
