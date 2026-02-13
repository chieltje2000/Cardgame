"""Request types for handling incoming requests."""

from dataclasses import dataclass

from .action import ActorAction, SystemAction


class Request:
    """Request object for handling incoming requests."""


@dataclass(frozen=True)
class InputRequest(Request):
    """Input request for handling actor input requests."""

    actor_id: object
    options: list[ActorAction]


@dataclass(frozen=True)
class SystemActionRequest(Request):
    """System request for handling system-level requests."""

    action: SystemAction


@dataclass(frozen=True)
class TerminalRequest(Request):
    """Terminal request for handling end-of-game requests."""

    outcome: object
