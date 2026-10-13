from todo_app.app import create_app


def test_create_app_has_layout():
    app = create_app()
    assert app.layout is not None
