"""Card types for the engine."""

class Card:
    """Represents a card entity (playing card or custom/trading card).

    Must NOT:
    - implement game rules
    - own engine orchestration
    """


class EffectCard(Card):
    """A card that can carry one or more effects.

    Must NOT:
    - execute effects by itself
    """
