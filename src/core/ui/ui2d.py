"""2D UI implementation (stub)."""

from __future__ import annotations

from core.engine.action import Action, ActorAction
from core.engine.observation import Observation

from .ui import UI


class UI2DEngine(UI):
    """2D UI stub (no real rendering yet)."""

    def render(self, observation: Observation) -> None:
        """Render an observation (stub)."""
        return None

    def choose_action(self, options: list[ActorAction]) -> Action:
        """Choose an ActorAction from options (stub)."""
        raise NotImplementedError("UI2DEngine.choose_action is not implemented yet.")
