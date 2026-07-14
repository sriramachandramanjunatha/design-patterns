# 📘 Setup Guide — Python + UV

## Why UV?
- 10–100x faster than pip
- Built-in virtual env management
- Single tool for deps, running, and locking
- Rust-based (from Astral, creators of Ruff)

## Java/Node → Python Mapping
| Concept | Java | Node | Python + UV |
|---------|------|------|-------------|
| Package manager | Maven/Gradle | npm | `uv` |
| Manifest file | `pom.xml` | `package.json` | `pyproject.toml` |
| Lock file | `gradle.lockfile` | `package-lock.json` | `uv.lock` |
| Install deps | `mvn install` | `npm install` | `uv sync` |
| Add dependency | edit pom | `npm i x` | `uv add x` |
| Run script | `java Main` | `node index.js` | `uv run python x.py` |
| Run tests | `mvn test` | `npm test` | `uv run pytest` |

## Commands Cheat Sheet
```bash
uv init                    # Initialize project
uv add <pkg>               # Add dependency
uv add --dev <pkg>         # Add dev dependency
uv sync                    # Install all deps
uv run python file.py      # Run a script
uv run pytest              # Run tests
uv lock                    # Update lock file
```

## Setup Steps Completed
1. ✅ Installed UV
2. ✅ Initialized project with `uv init`
3. ✅ Added pytest for testing
4. ✅ Created folder structure