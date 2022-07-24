from __future__ import annotations

from typing import Any

from AbstractHandler import AbstractHandler


class DogHandler(AbstractHandler):
    def ifood(self, request: Any) -> str | None:
        if request == "dog":
            return "I eat: meal, bone"
        else:
            return super().ifood(request)

    def handle(self, request: Any) -> str | None:
        if request == "bone":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)
