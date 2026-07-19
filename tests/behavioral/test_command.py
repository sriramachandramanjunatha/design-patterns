from src.behavioral.command import (
    Editor,
    InsertCommand,
    DeleteCommand,
    ReplaceCommand,
)


def test_insert_text():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello"))
    assert editor.document.content == "Hello"


def test_insert_multiple():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello"))
    editor.execute(InsertCommand(editor.document, 5, " World"))
    assert editor.document.content == "Hello World"


def test_delete_text():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello World"))
    editor.execute(DeleteCommand(editor.document, 5, 6))  # delete " World"
    assert editor.document.content == "Hello"


def test_undo_insert():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello"))
    assert editor.document.content == "Hello"

    editor.undo()
    assert editor.document.content == ""


def test_undo_delete():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello World"))
    editor.execute(DeleteCommand(editor.document, 5, 6))
    assert editor.document.content == "Hello"

    editor.undo()  # undo delete → restores " World"
    assert editor.document.content == "Hello World"


def test_redo():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello"))
    editor.undo()
    assert editor.document.content == ""

    editor.redo()
    assert editor.document.content == "Hello"


def test_multiple_undo_redo():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "A"))
    editor.execute(InsertCommand(editor.document, 1, "B"))
    editor.execute(InsertCommand(editor.document, 2, "C"))
    assert editor.document.content == "ABC"

    editor.undo()  # remove C
    editor.undo()  # remove B
    assert editor.document.content == "A"

    editor.redo()  # re-add B
    assert editor.document.content == "AB"


def test_new_action_clears_redo_stack():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello"))
    editor.undo()
    assert editor.can_redo is True

    editor.execute(InsertCommand(editor.document, 0, "World"))
    assert editor.can_redo is False  # redo cleared


def test_replace_command():
    editor = Editor()
    editor.execute(InsertCommand(editor.document, 0, "Hello World"))
    editor.execute(ReplaceCommand(editor.document, 6, 5, "Python"))
    assert editor.document.content == "Hello Python"

    editor.undo()  # undo replace
    assert editor.document.content == "Hello World"


def test_undo_returns_false_when_empty():
    editor = Editor()
    assert editor.undo() is False


def test_redo_returns_false_when_empty():
    editor = Editor()
    assert editor.redo() is False


def test_history_size():
    editor = Editor()
    assert editor.history_size == 0

    editor.execute(InsertCommand(editor.document, 0, "Hi"))
    assert editor.history_size == 1

    editor.undo()
    assert editor.history_size == 0