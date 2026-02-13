"""UI interface definitions."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.engine import Action, Observation
from core.engine.action import ActorAction


class UI(ABC):
    """Base UI interface.

    UI shows information and asks the user to choose an Action.

    Must NOT:
    - mutate game state directly
    - apply game rules or decide legality
    """

    @abstractmethod
    def render(self, observation: Observation) -> None:
        """Render a single observation for the current viewer."""
        raise NotImplementedError

    @abstractmethod
    def choose_action(self, options: list[ActorAction]) -> Action:
        """Choose one ActorAction from a list of legal options."""
        raise NotImplementedError

    def render_terminal(self, outcome: Any) -> None:
        """Render the terminal outcome (placeholder)."""
        return None
