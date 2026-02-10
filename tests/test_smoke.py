def test_import_core():
    import core
    import core.engine
    import core.ui


def test_public_engine_imports():
    from core.engine import (
        Game,
        Actor,
        Action,
        Event,
        Observation,
        Card,
        EffectCard,
        Effect,
        Zone,
        Deck,
        RNG,
    )
