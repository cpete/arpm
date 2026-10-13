from dash import Dash

from todo_app.callbacks import register_callbacks
from todo_app.layout import build_layout
from todo_app.store import TodoStore


def create_app() -> Dash:
    app = Dash(__name__, title="Todo List")
    store = TodoStore()
    app.layout = lambda: build_layout(store.list())
    register_callbacks(app, store)
    return app
