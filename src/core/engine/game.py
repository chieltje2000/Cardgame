"""Game definition interface for the engine."""

from .request import Request


class Game:
    """Game definition: rules + flow decisions.

    Must:
    - define what actions are legal
    - define how actions change state (later)
    - define what each actor can observe (later)

    Must NOT:
    - perform UI rendering
    - orchestrate the engine loop
    """

    def next_request(self) -> Request:
        """Return the next request.

        Must return an instance of one of the Request subtypes
        (InputRequest, SystemActionRequest, TerminalRequest).
        """
        raise NotImplementedError
