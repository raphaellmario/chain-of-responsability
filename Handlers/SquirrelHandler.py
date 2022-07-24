from __future__ import annotations

from typing import Any

from AbstractHandler import AbstractHandler


class SquirrelHandler(AbstractHandler):
    def ifood(self, request: Any) -> str | None:
        if request == "squirrel":
            return "I eat: nut, orange"
        else:
            return super().ifood(request)

    def handle(self, request: Any) -> str | None:
        if request == "nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)
