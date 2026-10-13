from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    text: str
    done: bool = False


class TodoStore:
    """In-memory todo storage."""

    def __init__(self) -> None:
        self._todos: list[Todo] = []
        self._next_id = 1

    def add(self, text: str) -> Todo:
        todo = Todo(self._next_id, text)
        self._next_id += 1
        self._todos.append(todo)
        return todo

    def list(self) -> list[Todo]:
        return list(self._todos)
