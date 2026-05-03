from dataclasses import dataclass
from pathlib import Path

from multi_agent_system.agents.base import AgentResult
from multi_agent_system.agents.code_analyzer import CodeAnalyzerAgent
from multi_agent_system.agents.documenter import DocumentAgent
from multi_agent_system.agents.planner import PlannerAgent
from multi_agent_system.agents.researcher import ResearchAgent
from multi_agent_system.agents.reviewer import ReviewerAgent
from multi_agent_system.agents.tester import TesterAgent
from multi_agent_system.memory import Memory
from multi_agent_system.token_plan import TokenPlan, build_token_plan
from multi_agent_system.tools.logger import save_run_log


@dataclass
class WorkflowResult:
    memory: Memory
    token_plan: TokenPlan
    agent_results: list[AgentResult]
    log_path: Path


class MultiAgentWorkflow:
    """Orchestrates long-chain reasoning through multiple specialized agents."""

    def __init__(self, project_path: str = ".") -> None:
        self.project_path = project_path
        self.agents = [
            PlannerAgent(),
            ResearchAgent(),
            CodeAnalyzerAgent(),
            TesterAgent(),
            DocumentAgent(),
            ReviewerAgent(),
        ]

    def run(self, task: str) -> WorkflowResult:
        memory = Memory(task=task)
        memory.set("project_path", self.project_path)

        token_plan = build_token_plan(task)
        memory.set("token_plan", token_plan)

        agent_results = []
        for agent in self.agents:
            memory.add_trace(f"Start {agent.name}.")
            result = agent.run(memory)
            agent_results.append(result)
            memory.add_trace(f"Finish {agent.name}: {result.summary}")

        log_path = save_run_log(memory, token_plan, agent_results)

        return WorkflowResult(
            memory=memory,
            token_plan=token_plan,
            agent_results=agent_results,
            log_path=log_path,
        )
