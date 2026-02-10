# Cardgame Engine

Generic cardgame engine in Python.

## Status

version 0.1.0

✅ Sprint 1 — Engine skeleton: **DONE**

- `core.engine` skeleton classes (no engine loop yet)
- `core.ui` interface + stub implementations
- Public API exports
- Ruff + Pytest configured
- GitHub Actions CI added (ruff + pytest)

🚧 Sprint 2 — Request model: **READY TO START**

- PlayerAction vs SystemAction separation
- Request types (Input/System/Terminal)
- Meaningful tests + public exports

## Quickstart (dev)

### Requirements

- Python **>= 3.11**
- Git

### Setup

```bash
python -m venv .venv


# Windows (PowerShell/CMD):
.venv\Scripts\activate

# macOS/Linux:
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e ".[dev]"
```
