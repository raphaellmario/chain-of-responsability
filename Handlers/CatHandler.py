from __future__ import annotations

from typing import Any

from AbstractHandler import AbstractHandler


class CatHandler(AbstractHandler):
    def ifood(self, request: Any) -> str | None:
        if request == "cat":
            return "I eat: milk, fish"
        else:
            return super().ifood(request)

    def handle(self, request: Any) -> str | None:
        if request == "fish":
            return f"cat: I'll eat the {request}"
        else:
            return super().handle(request)
