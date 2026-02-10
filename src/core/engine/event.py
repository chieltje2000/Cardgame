class Event:
    """Represents a fact that happened as a result of applying an action.

    Must NOT:
    - encode UI rendering
    - contain hidden mutation logic
    """
    