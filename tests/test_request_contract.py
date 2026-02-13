from core.engine.request import InputRequest, Request, SystemActionRequest, TerminalRequest


def test_request_subtypes_are_markers():
    assert issubclass(InputRequest, Request)
    assert issubclass(SystemActionRequest, Request)
    assert issubclass(TerminalRequest, Request)


def test_request_subtypes_are_distinct():
    assert not issubclass(SystemActionRequest, InputRequest)
    assert not issubclass(InputRequest, SystemActionRequest)
    assert not issubclass(TerminalRequest, InputRequest)
    assert not issubclass(InputRequest, TerminalRequest)
    assert not issubclass(TerminalRequest, SystemActionRequest)
    assert not issubclass(SystemActionRequest, TerminalRequest)


def test_inputRequest_options_are_list_of_actor_actions():
    from core.engine.action import ActorAction, SystemAction

    req_ok = InputRequest(actor_id=object(), options=[ActorAction()])
    assert all(isinstance(o, ActorAction) for o in req_ok.options)

    req_bad = InputRequest(actor_id=object(), options=[ActorAction(), SystemAction()])
    assert not all(isinstance(o, ActorAction) for o in req_bad.options)


def test_systemActionRequest_action_is_system_action():
    from core.engine.action import ActorAction, SystemAction

    req_ok = SystemActionRequest(action=SystemAction())
    assert isinstance(req_ok.action, SystemAction)

    req_bad = SystemActionRequest(action=ActorAction())
    assert not isinstance(req_bad.action, SystemAction)


def test_engine_request_does_not_import_ui():
    import sys

    import core.engine.request as _  # noqa: F401

    assert not any(m == "core.ui" or m.startswith("core.ui.") for m in sys.modules)
