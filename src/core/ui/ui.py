from abc import ABC, abstractmethod
from typing import Any

from core.engine import Action, Observation


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
    def choose_action(self, options: list[Action]) -> Action:
        """Choose one action from a list of legal options."""
        raise NotImplementedError

    def render_terminal(self, outcome: Any) -> None:
        """Optional: render terminal outcome (placeholder)."""
        return None
