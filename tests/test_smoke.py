def test_import_core():
    import core

    _ = (core.engine, core.ui)


def test_public_engine_imports():
    import core.engine as engine

    _ = (
        engine.Game,
        engine.Actor,
        engine.Action,
        engine.Event,
        engine.Observation,
        engine.Card,
        engine.EffectCard,
        engine.Effect,
        engine.Zone,
        engine.Deck,
        engine.RNG,
    )


def test_public_ui_imports():
    import core.ui as ui

    _ = (ui.UI, ui.UICLI, ui.UI2DEngine)
