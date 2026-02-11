from core.engine.action import Action, ActorAction, SystemAction


def test_action_subtypes_are_markers():
    assert issubclass(ActorAction, Action)
    assert issubclass(SystemAction, Action)


def test_action_subtypes_are_distinct():
    assert not issubclass(SystemAction, ActorAction)
    assert not issubclass(ActorAction, SystemAction)
