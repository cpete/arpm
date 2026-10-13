from dash import Dash

from todo_app.callbacks import register_callbacks
from todo_app.layout import build_layout


def create_app() -> Dash:
    app = Dash(__name__, title="Todo List")
    app.layout = build_layout()
    register_callbacks(app)
    return app
