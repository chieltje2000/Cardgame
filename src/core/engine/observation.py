class Observation:
    """A view of the current state for a specific actor (what they are allowed to see).

    Must NOT:
    - leak hidden/private information unintentionally
    - mutate state
    """