from core.engine import Action, Observation

from .ui import UI


class UICLI(UI):
    """CLI UI stub (no real rendering yet)."""

    def render(self, observation: Observation) -> None:
        return None

    def choose_action(self, options: list[Action]) -> Action:
        raise NotImplementedError("UICLI.choose_action is not implemented yet.")
