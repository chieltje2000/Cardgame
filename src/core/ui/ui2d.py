from core.engine import Action, Observation

from .ui import UI


class UI2DEngine(UI):
    """2D UI stub (no real rendering yet)."""

    def render(self, observation: Observation) -> None:
        return None

    def choose_action(self, options: list[Action]) -> Action:
        raise NotImplementedError("UI2DEngine.choose_action is not implemented yet.")
