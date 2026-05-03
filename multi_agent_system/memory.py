from dataclasses import dataclass, field
from typing import Any


@dataclass
class Memory:
    """A lightweight shared memory for all agents."""

    task: str
    data: dict[str, Any] = field(default_factory=dict)
    trace: list[str] = field(default_factory=list)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def add_trace(self, message: str) -> None:
        self.trace.append(message)
