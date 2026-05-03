from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from multi_agent_system.memory import Memory


@dataclass
class AgentResult:
    agent_name: str
    summary: str
    details: dict[str, Any]

    def to_markdown(self) -> str:
        lines = [
            f"## {self.agent_name}",
            "",
            f"**Summary:** {self.summary}",
            "",
        ]
        for key, value in self.details.items():
            lines.append(f"### {key}")
            if isinstance(value, list):
                lines.extend([f"- {item}" for item in value])
            elif isinstance(value, dict):
                for k, v in value.items():
                    lines.append(f"- **{k}:** {v}")
            else:
                lines.append(str(value))
            lines.append("")
        return "\n".join(lines)


class BaseAgent(ABC):
    name = "Base Agent"

    @abstractmethod
    def run(self, memory: Memory) -> AgentResult:
        raise NotImplementedError
