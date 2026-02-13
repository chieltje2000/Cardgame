def test_next_request_is_request():
    from core.engine.game import Game
    from core.engine.request import Request, TerminalRequest

    class TestGame(Game):
        def next_request(self) -> Request:
            return TerminalRequest(outcome=object())

    game = TestGame()
    req_out = game.next_request()
    assert isinstance(req_out, Request)
