from todo_app.app import create_app


def main() -> None:
    create_app().run(debug=True)


if __name__ == "__main__":
    main()
