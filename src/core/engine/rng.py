"""Randomness interface for the engine."""

class RNG:
    """Provides randomness in a controllable/testable way.

    Must NOT:
    - be a global singleton
    - hide non-determinism from tests
    """
