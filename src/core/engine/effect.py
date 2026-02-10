class Effect:
    """Represents a reusable effect that may be attached to cards or rules.

    Must NOT:
    - directly orchestrate engine flow
    - be tied to a specific game implementation
    """