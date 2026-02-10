class Zone:
    """A container for cards (e.g., hand, deck, discard, battlefield).

    Must NOT:
    - enforce game rules
    - decide visibility/observation by itself
    """


class Deck(Zone):
    """A zone representing a draw pile.

    Must NOT:
    - implement shuffling policy beyond generic operations (later)
    """