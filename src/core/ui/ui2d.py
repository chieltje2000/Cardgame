"""2D UI implementation (stub)."""

from __future__ import annotations

from core.engine import Action, Observation

from .ui import UI


class UI2DEngine(UI):
    """2D UI stub (no real rendering yet)."""

    def render(self, observation: Observation) -> None:
        """Render an observation (stub)."""
        return None

    def choose_action(self, options: list[Action]) -> Action:
        """Choose an action from options (stub)."""
        raise NotImplementedError("UI2DEngine.choose_action is not implemented yet.")
