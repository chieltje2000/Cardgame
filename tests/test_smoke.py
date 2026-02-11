def test_import_core():
    from core import engine, ui

    _ = (engine, ui)


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


def test_public_engine_action_exports():
    from core.engine import Action, ActorAction, SystemAction

    _ = (Action, ActorAction, SystemAction)


def test_public_ui_imports():
    import core.ui as ui

    _ = (ui.UI, ui.UICLI, ui.UI2DEngine)


def test_minimal_construction():
    import core.engine as engine
    import core.ui as ui

    # engine: construct where it has no required dependencies
    engine.Action()
    engine.Event()
    engine.Actor()
    engine.Observation()
    engine.Effect()
    engine.Card()
    engine.EffectCard()
    engine.Zone()
    engine.Deck()
    engine.RNG()

    # ui: concrete stubs should be instantiable
    ui.UICLI()
    ui.UI2DEngine()
