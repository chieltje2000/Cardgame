"""Action types for the engine.

Actions represent *intent* and are passed through the engine pipeline.

Invariants:
- Actions must NOT mutate game state directly.
- Actions must NOT contain game-specific rule logic.
"""

from __future__ import annotations


class Action:
    """Base type for all actions.

    This is a marker/base class. Concrete games may subtype this further.
    """


class ActorAction(Action):
    """Action that MAY be offered to an actor decision provider (UI / AI).

    Examples:
    - "Play card X"
    - "Draw a card"

    """


class SystemAction(Action):
    """Action that MUST NOT be offered as a choice to any actor.

    This may still be rendered in UI output/logging, but never as an input option.

    Examples:
    - "Shuffle deck"
    - "Deal opening hand"

    """
