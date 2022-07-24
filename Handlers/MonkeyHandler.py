from __future__ import annotations

import array
from typing import Any

from AbstractHandler import AbstractHandler


class MonkeyHandler(AbstractHandler):
    def ifood(self, request: Any) -> str | None:
        if request == "monkey":
            return "I eat: banana, apple"
        else:
            return super().ifood(request)

    def handle(self, request: Any) -> str | None:
        if request == "banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)
