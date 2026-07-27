# 03 — Command Pattern

## 🎯 Problem
A text editor needs undo/redo. Each action (insert, delete, replace) must be
reversible. Hard-coding undo logic per action creates tangled, untestable code.

## ✅ Solution
Encapsulate each action as a **Command object** with `execute()` and `undo()`.
An **Invoker** (Editor) maintains a history stack for undo and a redo stack.

## Key Insight
Command is everywhere: "Every Git commit is a command with undo (revert). Every Redux action is a command dispatched to a reducer. Every DB migration has up() and down(). Undo/redo in any editor is a command history stack.".


## 🏗️ Structure
```
Command (ABC)
├── execute()
└── undo()

InsertCommand ──┐
DeleteCommand  ──┼── implement Command
ReplaceCommand ──┘    (ReplaceCommand composes Delete + Insert)

Editor (Invoker)
├── execute(command) → pushes to history
├── undo()           → pops history, pushes to redo
└── redo()           → pops redo, pushes to history

Document (Receiver)
├── insert(pos, text)
└── delete(pos, length)
```

## 🐍 Pythonic Notes (vs Java/Node)
| Aspect | Java | Node | Python |
|--------|------|------|--------|
| Command interface | `interface Command` | callback/closure | `ABC` |
| Invoker | `CommandManager` class | middleware stack | `Editor` class |
| Undo data | stored in command fields | closure captures | `self._deleted_text` |
| Composite cmd | `MacroCommand` class | promise chain | `ReplaceCommand` composes two commands |

> **Java parallel:** Swing's `UndoManager` / `AbstractUndoableEdit` is exactly this pattern.

> **Node parallel:** Express middleware `next()` chains, Redux action dispatching,
> and task queues (Bull/BullMQ) all use Command concepts.

## When to Use
- **Undo/redo** — classic use case
- **Task queues** — serialize commands for later execution
- **Macro recording** — batch multiple commands
- **Transactional operations** — rollback on failure
- **Audit logging** — every action is a recorded object

## When NOT to Use
- Simple one-off operations (overkill)
- No need for undo, queuing, or logging

## Real-World Examples
- Text editors (VS Code, IntelliJ)
- Database migrations (each migration = a command with up/down)
- Git commits (each commit is a reversible command)
- Redux actions (dispatch → reducer → state)
- CI/CD pipelines (each step = a command)

## Interview Q&A

**Q: Command vs Strategy?**
A: **Strategy** = swap algorithms for the *same task*.
**Command** = encapsulate *different tasks* as objects (with history/undo).

**Q: How does Command enable undo?**
A: Each command stores enough state to reverse itself. The invoker
maintains a stack — `undo()` pops and calls `command.undo()`.

**Q: What about redo?**
A: Undone commands are pushed to a redo stack. A new `execute()` clears
the redo stack (divergent timeline).

**Q: Command vs Event Sourcing?**
A: Related! Event sourcing stores every state change as an immutable event.
Command pattern stores reversible actions. Event sourcing = append-only log;
Command = bidirectional (execute + undo).

**Q: How would you implement a macro (batch) command?**
A: Create a `MacroCommand` that holds a list of commands. Its `execute()` runs
all in order; `undo()` runs all in reverse. Our `ReplaceCommand` does this —
it composes `DeleteCommand` + `InsertCommand`.

## Run
```bash
uv run pytest tests/behavioral/test_command.py -v
```