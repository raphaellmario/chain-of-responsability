from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

from Handler import Handler


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> None:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

    @abstractmethod
    def ifood(self, request: Any) -> None:
        if self._next_handler:
            return self._next_handler.ifood(request)

        return None
