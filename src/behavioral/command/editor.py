"""
Command Pattern — Real-world: Text editor with undo/redo.

Java devs: think Runnable/Callable with execute() + undo().
Node devs: think middleware chains or task queues.

Each action is an object with execute() and undo(), pushed onto a history stack.
"""
from abc import ABC, abstractmethod


# --- Receiver: the object being acted upon ---
class Document:
    def __init__(self) -> None:
        self._content: list[str] = []

    @property
    def content(self) -> str:
        return "".join(self._content)

    def insert(self, position: int, text: str) -> None:
        self._content.insert(position, text)

    def delete(self, position: int, length: int) -> str:
        deleted = []
        for _ in range(length):
            if position < len(self._content):
                deleted.append(self._content.pop(position))
        return "".join(deleted)

    def __repr__(self) -> str:
        return f'Document("{self.content}")'


# --- Command Interface ---
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...

    @abstractmethod
    def undo(self) -> None:
        ...


# --- Concrete Commands ---
class InsertCommand(Command):
    def __init__(self, document: Document, position: int, text: str) -> None:
        self._document = document
        self._position = position
        self._text = text

    def execute(self) -> None:
        for i, char in enumerate(self._text):
            self._document.insert(self._position + i, char)

    def undo(self) -> None:
        self._document.delete(self._position, len(self._text))


class DeleteCommand(Command):
    def __init__(self, document: Document, position: int, length: int) -> None:
        self._document = document
        self._position = position
        self._length = length
        self._deleted_text: str = ""  # saved for undo

    def execute(self) -> None:
        self._deleted_text = self._document.delete(self._position, self._length)

    def undo(self) -> None:
        for i, char in enumerate(self._deleted_text):
            self._document.insert(self._position + i, char)


class ReplaceCommand(Command):
    """Composite command: delete old text, insert new text."""

    def __init__(
        self, document: Document, position: int, length: int, new_text: str
    ) -> None:
        self._delete_cmd = DeleteCommand(document, position, length)
        self._insert_cmd = InsertCommand(document, position, new_text)

    def execute(self) -> None:
        self._delete_cmd.execute()
        self._insert_cmd.execute()

    def undo(self) -> None:
        self._insert_cmd.undo()
        self._delete_cmd.undo()


# --- Invoker: manages history + undo/redo ---
class Editor:
    def __init__(self) -> None:
        self.document = Document()
        self._history: list[Command] = []
        self._redo_stack: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self._history.append(command)
        self._redo_stack.clear()  # new action invalidates redo

    def undo(self) -> bool:
        if not self._history:
            return False
        command = self._history.pop()
        command.undo()
        self._redo_stack.append(command)
        return True

    def redo(self) -> bool:
        if not self._redo_stack:
            return False
        command = self._redo_stack.pop()
        command.execute()
        self._history.append(command)
        return True

    @property
    def can_undo(self) -> bool:
        return len(self._history) > 0

    @property
    def can_redo(self) -> bool:
        return len(self._redo_stack) > 0

    @property
    def history_size(self) -> int:
        return len(self._history)